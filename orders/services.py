from decimal import Decimal
from itertools import permutations

from boxes.models import Box

#1. Return all unique orientations of a product.
def get_product_orientations(product):
    

    dimensions = (
        product.length,
        product.width,
        product.height,
    )

    return list(set(permutations(dimensions)))

#2. Convert OrderItems with quantities into individual product references for packing.
def expand_order_items(order):
    products = []

    for order_item in order.items.select_related("product"):
        for _ in range(order_item.quantity):
            products.append(order_item.product)

    return products


#3. Calculate the total weight of all products in the order.
def calculate_total_weight(order):

    total_weight = Decimal("0")

    for order_item in order.items.select_related("product"):
        total_weight += (
            order_item.product.weight * order_item.quantity
        )

    return total_weight

#4. Calculate the overall bounding-box dimensions of all packed items.
def calculate_bounding_dimensions(packed_items):
    if not packed_items:
        return (
            Decimal("0"),
            Decimal("0"),
            Decimal("0"),
        )

    max_x = max(
        item["x"] + item["length"]
        for item in packed_items
    )

    max_y = max(
        item["y"] + item["width"]
        for item in packed_items
    )

    max_z = max(
        item["z"] + item["height"]
        for item in packed_items
    )

    return max_x, max_y, max_z


#5. Check whether two 3D rectangular items overlap.
def boxes_overlap(item_a, item_b):
    
    separated_on_x = (
        item_a["x"] + item_a["length"] <= item_b["x"]
        or
        item_b["x"] + item_b["length"] <= item_a["x"]
    )

    separated_on_y = (
        item_a["y"] + item_a["width"] <= item_b["y"]
        or
        item_b["y"] + item_b["width"] <= item_a["y"]
    )

    separated_on_z = (
        item_a["z"] + item_a["height"] <= item_b["z"]
        or
        item_b["z"] + item_b["height"] <= item_a["z"]
    )

    return not (
        separated_on_x
        or separated_on_y
        or separated_on_z
    )

#6. Check whether a candidate placement overlaps any already packed item.
def position_is_valid(candidate, packed_items):
    
    for packed_item in packed_items:
        if boxes_overlap(candidate, packed_item):
            return False

    return True

#7. Generate positions adjacent to already packed items.
def generate_candidate_positions(packed_items):

    positions = {
        (
            Decimal("0"),
            Decimal("0"),
            Decimal("0"),
        )
    }

    for item in packed_items:
        positions.add(
            (
                item["x"] + item["length"],
                item["y"],
                item["z"],
            )
        )

        positions.add(
            (
                item["x"],
                item["y"] + item["width"],
                item["z"],
            )
        )

        positions.add(
            (
                item["x"],
                item["y"],
                item["z"] + item["height"],
            )
        )

    return sorted(positions)

#8. Pack all products using a deterministic greedy 3D placement heuristic with rotation support.
def pack_products(order):
    
    products = expand_order_items(order)

    if not products:
        raise ValueError("Order must contain at least one item.")

    # Place larger products first.
    products.sort(
        key=lambda product: (
            product.length
            * product.width
            * product.height
        ),
        reverse=True,
    )

    packed_items = []

    for product in products:
        best_placement = None
        best_volume = None

        orientations = get_product_orientations(product)

        candidate_positions = generate_candidate_positions(
            packed_items
        )

        for orientation in orientations:

            length, width, height = orientation

            for x, y, z in candidate_positions:

                candidate = {
                    "x": x,
                    "y": y,
                    "z": z,
                    "length": length,
                    "width": width,
                    "height": height,
                }

                if not position_is_valid(
                    candidate,
                    packed_items
                ):
                    continue

                test_items = packed_items + [candidate]

                bounding_dimensions = (
                    calculate_bounding_dimensions(
                        test_items
                    )
                )

                bounding_volume = (
                    bounding_dimensions[0]
                    * bounding_dimensions[1]
                    * bounding_dimensions[2]
                )

                if (
                    best_volume is None
                    or bounding_volume < best_volume
                ):
                    best_volume = bounding_volume
                    best_placement = candidate

        if best_placement is None:
            raise ValueError(
                f"Unable to pack product: {product.name}"
            )

        packed_items.append(best_placement)

    return calculate_bounding_dimensions(packed_items)

#9. Check whether the packed dimensions fit inside the box in any orientation.
def fits_in_box(packed_dimensions, box):
    
    return any(
        all(
            packed_dimension <= box_dimension
            for packed_dimension, box_dimension
            in zip(
                orientation,
                (
                    box.length,
                    box.width,
                    box.height,
                ),
            )
        )
        for orientation in permutations(
            packed_dimensions
        )
    )

#10. Calculate unused volume inside the box.
def calculate_wasted_volume(box, packed_dimensions):
    
    box_volume = (
        box.length
        * box.width
        * box.height
    )

    packed_volume = (
        packed_dimensions[0]
        * packed_dimensions[1]
        * packed_dimensions[2]
    )

    return box_volume - packed_volume

#11. Recommend the most suitable box for an order.
def recommend_box(order):
    
    packed_dimensions = pack_products(order)

    total_weight = calculate_total_weight(order)

    eligible_boxes = []

    for box in Box.objects.all():

        # Physical fit
        if not fits_in_box(
            packed_dimensions,
            box
        ):
            continue

        # Weight capacity
        if total_weight > box.max_weight:
            continue

        wasted_volume = calculate_wasted_volume(
            box,
            packed_dimensions
        )

        eligible_boxes.append(
            {
                "box": box,
                "wasted_volume": wasted_volume,
            }
        )

    if not eligible_boxes:
        return None

    eligible_boxes.sort(
        key=lambda candidate: (
            candidate["box"].cost,
            candidate["wasted_volume"],
            candidate["box"].id,
        )
    )

    return {
        "box": eligible_boxes[0]["box"],
        "total_weight": total_weight,
        "packed_dimensions": packed_dimensions,
        "wasted_volume": eligible_boxes[0]["wasted_volume"],
    }