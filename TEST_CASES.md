# Test Cases

This document describes the automated test cases implemented for the
AI-Assisted Box Selection System.

## Test Execution

The tests are implemented using Django's built-in testing framework.

Command used:

```bash
python manage.py test
```

## Automated Test Cases

The project includes automated tests covering the core order, packing, box-selection, and API functionality.

| Test ID | Test Case | Description | Expected Result |
|---|---|---|---|
| TC01 | Create order with items | Creates an order and adds a product with a specified quantity. | Order is created and contains the correct item and quantity. |
| TC02 | Calculate total order weight | Calculates the total weight based on product weight and quantity. | Total weight equals product weight multiplied by quantity. |
| TC03 | Pack a single product | Packs an order containing one product. | The packed bounding dimensions match the product dimensions. |
| TC04 | Pack multiple quantities | Packs multiple units of the same product. | All product units are packed and valid bounding dimensions are calculated. |
| TC05 | Product rotation | Checks whether a product can fit into a box when its orientation is changed. | The product can fit when rotation is required. |
| TC06 | Cheapest eligible box | Tests box selection when multiple suitable boxes are available at different costs. | The lowest-cost eligible box is selected. |
| TC07 | Weight capacity check | Tests a box whose maximum weight is lower than the order's total weight. | The box exceeding the weight requirement is not selected. |
| TC08 | Dimension fit check | Tests a box whose dimensions are too small for the order. | The box that cannot contain the packed products is not selected. |
| TC09 | No suitable box | Tests an order for which no available box satisfies the requirements. | The recommendation function returns no box. |
| TC10 | Equal-cost box selection | Tests multiple eligible boxes with the same cost but different wasted space. | The box with less wasted space is selected. |
| TC11 | Empty order | Tests box recommendation for an order containing no items. | A `ValueError` is raised indicating that the order must contain at least one item. |
| TC12 | Nested order creation API | Creates an order through the REST API with product items included in the request. | The API returns HTTP `201` and creates the order with the specified items. |
| TC13 | Box recommendation API | Sends a POST request to the box recommendation endpoint for an order. | The API returns HTTP `200` and provides a recommended box. |

## Test Coverage

The test suite covers the main functionality of the system, including:

- Order and order-item creation
- Product quantity handling
- Total order weight calculation
- Product packing
- Product rotation
- Box dimension validation
- Box weight-capacity validation
- Cost-based box selection
- Wasted-space comparison
- Handling orders with no items
- Handling cases where no suitable box is available
- Nested order creation through the REST API
- Box recommendation through the REST API

## Test Result

The final test result is recorded separately in [`TEST_OUTPUT.md`](TEST_OUTPUT.md).

## Test Count

The automated test suite contains **13 test cases**, from `TC01` through `TC13`.