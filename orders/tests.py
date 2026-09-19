from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from boxes.models import Box
from products.models import Product

from .models import Order
from .services import (
    calculate_total_weight,
    fits_in_box,
    pack_products,
    recommend_box,
)


class OrderModelTests(TestCase):
    """Tests for Order and OrderItem behavior."""

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2,
        )

    def test_create_order_with_items(self):
        order = Order.objects.create()

        order.items.create(
            product=self.product,
            quantity=2,
        )

        self.assertEqual(order.items.count(), 1)
        self.assertEqual(
            order.items.first().quantity,
            2,
        )

    def test_total_weight_calculation(self):
        order = Order.objects.create()

        order.items.create(
            product=self.product,
            quantity=3,
        )

        total_weight = calculate_total_weight(order)

        self.assertEqual(
            total_weight,
            Decimal("6.00"),
        )


class OrderPackingTests(TestCase):
    """Tests for the product packing logic."""

    def test_single_product_packing(self):
        product = Product.objects.create(
            name="Book",
            length=10,
            width=10,
            height=5,
            weight=1,
        )

        order = Order.objects.create()

        order.items.create(
            product=product,
            quantity=1,
        )

        packed_dimensions = pack_products(order)

        self.assertEqual(
            packed_dimensions,
            (
                Decimal("10.00"),
                Decimal("10.00"),
                Decimal("5.00"),
            ),
        )

    def test_multiple_quantity_packing(self):
        product = Product.objects.create(
            name="Small Box",
            length=5,
            width=5,
            height=5,
            weight=1,
        )

        order = Order.objects.create()

        order.items.create(
            product=product,
            quantity=2,
        )

        packed_dimensions = pack_products(order)

        self.assertEqual(
            sorted(packed_dimensions),
            sorted(
                (
                    Decimal("10.00"),
                    Decimal("5.00"),
                    Decimal("5.00"),
                )
            ),
        )

    def test_product_rotation_is_supported(self):
        product = Product.objects.create(
            name="Rotated Product",
            length=20,
            width=10,
            height=5,
            weight=1,
        )

        box = Box.objects.create(
            name="Rotated Box",
            length=10,
            width=20,
            height=5,
            max_weight=10,
            cost=50,
        )

        order = Order.objects.create()

        order.items.create(
            product=product,
            quantity=1,
        )

        packed_dimensions = pack_products(order)

        self.assertTrue(
            fits_in_box(
                packed_dimensions,
                box,
            )
        )


class BoxRecommendationTests(TestCase):
    """Tests for the box recommendation business logic."""

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=20,
            width=15,
            height=5,
            weight=2,
        )

        self.order = Order.objects.create()

        self.order.items.create(
            product=self.product,
            quantity=1,
        )

    def test_recommendation_selects_cheapest_eligible_box(self):
        Box.objects.create(
            name="Expensive Box",
            length=25,
            width=20,
            height=10,
            max_weight=10,
            cost=100,
        )

        cheap_box = Box.objects.create(
            name="Cheap Box",
            length=22,
            width=17,
            height=7,
            max_weight=10,
            cost=50,
        )

        result = recommend_box(self.order)

        self.assertIsNotNone(result)
        self.assertEqual(
            result["box"].id,
            cheap_box.id,
        )

    def test_box_exceeding_weight_limit_is_not_selected(self):
        heavy_product = Product.objects.create(
            name="Heavy Product",
            length=10,
            width=10,
            height=10,
            weight=15,
        )

        order = Order.objects.create()

        order.items.create(
            product=heavy_product,
            quantity=1,
        )

        Box.objects.create(
            name="Light Capacity Box",
            length=20,
            width=20,
            height=20,
            max_weight=10,
            cost=20,
        )

        suitable_box = Box.objects.create(
            name="Heavy Capacity Box",
            length=20,
            width=20,
            height=20,
            max_weight=20,
            cost=40,
        )

        result = recommend_box(order)

        self.assertIsNotNone(result)
        self.assertEqual(
            result["box"].id,
            suitable_box.id,
        )

    def test_box_that_does_not_fit_is_not_selected(self):
        Box.objects.create(
            name="Too Small Box",
            length=10,
            width=10,
            height=4,
            max_weight=10,
            cost=10,
        )

        suitable_box = Box.objects.create(
            name="Large Box",
            length=25,
            width=20,
            height=10,
            max_weight=10,
            cost=50,
        )

        result = recommend_box(self.order)

        self.assertIsNotNone(result)
        self.assertEqual(
            result["box"].id,
            suitable_box.id,
        )

    def test_no_suitable_box_returns_none(self):
        Box.objects.create(
            name="Too Small Box",
            length=5,
            width=5,
            height=5,
            max_weight=10,
            cost=10,
        )

        result = recommend_box(self.order)

        self.assertIsNone(result)

    def test_equal_cost_prefers_less_wasted_space(self):
        smaller_box = Box.objects.create(
            name="Smaller Box",
            length=22,
            width=17,
            height=7,
            max_weight=10,
            cost=50,
        )

        Box.objects.create(
            name="Larger Box",
            length=30,
            width=25,
            height=15,
            max_weight=10,
            cost=50,
        )

        result = recommend_box(self.order)

        self.assertIsNotNone(result)
        self.assertEqual(
            result["box"].id,
            smaller_box.id,
        )

    def test_empty_order_raises_error(self):
        empty_order = Order.objects.create()

        with self.assertRaises(ValueError):
            recommend_box(empty_order)


class OrderAPITests(TestCase):
    """Tests for the Order REST API."""

    def setUp(self):
        self.client = APIClient()

        self.product = Product.objects.create(
            name="Keyboard",
            length=40,
            width=15,
            height=5,
            weight=1,
        )

    def test_create_order_with_nested_items(self):
        response = self.client.post(
            "/api/orders/",
            {
                "items": [
                    {
                        "product": self.product.id,
                        "quantity": 2,
                    }
                ]
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            201,
        )

        self.assertEqual(
            response.data["items"][0]["product"],
            self.product.id,
        )

        self.assertEqual(
            response.data["items"][0]["quantity"],
            2,
        )

    def test_recommend_box_api(self):
        Box.objects.create(
            name="API Test Box",
            length=50,
            width=25,
            height=10,
            max_weight=10,
            cost=40,
        )

        order = Order.objects.create()

        order.items.create(
            product=self.product,
            quantity=1,
        )

        response = self.client.post(
            f"/api/orders/{order.id}/recommend-box/"
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertIsNotNone(
            response.data["recommended_box"]
        )