# AI-Assisted Box Selection System

A Django-based system that recommends a suitable shipping box for an e-commerce order based on product dimensions, product weight, box dimensions, box weight capacity, cost, and available packing space.

The system supports multiple products and quantities within an order and uses a simplified 3D packing heuristic with product rotation support to estimate the required packing dimensions.

---

## 1. Project Overview

In an e-commerce warehouse, selecting the appropriate shipping box for an order is important for handling products safely while avoiding unnecessary packaging space and cost.

This project provides a backend system that:

- Stores product specifications.
- Stores supported shipping box specifications.
- Creates orders containing multiple products and quantities.
- Calculates the total weight of an order.
- Packs products using a simplified 3D packing heuristic.
- Considers product rotation while packing.
- Checks whether the packed products fit inside available boxes.
- Checks whether the box can support the total order weight.
- Recommends a suitable box based on cost and wasted space.

---

## 2. Problem Statement

For each customer order, the warehouse needs to determine which available shipping box can contain all the ordered products while satisfying the box's maximum weight capacity.

The system must consider:

1. Product dimensions.
2. Product weight.
3. Product quantity.
4. Multiple products in the same order.
5. Product rotation during packing.
6. Box internal dimensions.
7. Box maximum weight capacity.
8. Box cost.
9. Wasted space inside the selected box.

---

## 3. Features

### Product Management

Products contain:

- Name
- Length
- Width
- Height
- Weight

Products can be created, viewed, updated, and deleted through the REST API.

### Box Management

Boxes contain:

- Name
- Internal length
- Internal width
- Internal height
- Maximum weight capacity
- Cost

Boxes can be created, viewed, updated, and deleted through the REST API.

### Order Management

An order can contain multiple products with different quantities.

Orders are created using a nested request structure, for example:

```json
{
    "items": [
        {
            "product": 1,
            "quantity": 2
        },
        {
            "product": 2,
            "quantity": 1
        }
    ]
}
```


## Box Recommendation
The system evaluates available boxes and recommends a suitable box based on:

- Whether all packed products fit inside the box.
- Whether the total order weight is within the box's maximum weight capacity.
- Box cost.
- Wasted space

---

## 4. Technology Stack
- Backend: Python, Django
- API: Django REST Framework
- Database: SQLite
- Configuration: python-dotenv
- Testing: Django Test Framework and Django REST Framework API testing utilities
- Version Control: Git and GitHub

## 5. Project Structure
```text

AI-Assisted-Box-Selection-System/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── boxes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── services.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── .gitignore
├── .env
├── README.md
├── AI_USAGE.md
├── TEST_CASES.md
└── TEST_OUTPUT.md

```
---

## 6. Database Design
The system uses four main database tables:

### Product
Stores the physical specifications and weight of each product.

```text

Product
--------
id
name
length
width
height
weight

```

### Box

Stores the specifications of each supported shipping box.

```text

Box
---
id
name
length
width
height
max_weight
cost

```

### Order
Represents a customer order.

```text

Order
-----
id
created_at

```

### OrderItem
Connects products to orders and stores the quantity of each product.

```text

OrderItem
---------
id
order_id
product_id
quantity

```

### Relationships
```text

Product 1 ──────── N OrderItem N ──────── 1 Order

Box
 │
 └── Independent box catalogue

```

A product can appear in many order items, and an order can contain many order items.

Boxes are maintained independently because they represent the types of shipping boxes supported by the business.

---

## 7. Django Admin

Django's built-in Admin interface is used as a lightweight management interface for maintaining:

- Products
- Boxes
- Orders
- Order items

The recommendation logic does not depend on Django Admin.

The Admin interface can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

A Django superuser is required to access the Admin interface.

Create one using:

```bash
python manage.py createsuperuser
```

---

## 8. API Endpoints

### Products

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create a product |
| GET | `/api/products/<id>/` | Retrieve a product |
| PUT/PATCH | `/api/products/<id>/` | Update a product |
| DELETE | `/api/products/<id>/` | Delete a product |

### Boxes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/boxes/` | List all boxes |
| POST | `/api/boxes/` | Create a box |
| GET | `/api/boxes/<id>/` | Retrieve a box |
| PUT/PATCH | `/api/boxes/<id>/` | Update a box |
| DELETE | `/api/boxes/<id>/` | Delete a box |

### Orders

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/orders/` | List all orders |
| POST | `/api/orders/` | Create an order with nested items |
| GET | `/api/orders/<id>/` | Retrieve an order |
| POST | `/api/orders/<id>/recommend-box/` | Recommend a suitable box |

The recommendation endpoint accepts **POST** requests.

---

## 9. Creating an Order

Use:

```text
POST /api/orders/
```

Example request:

```json
{
    "items": [
        {
            "product": 1,
            "quantity": 2
        },
        {
            "product": 2,
            "quantity": 1
        }
    ]
}
```

The response contains the created order and its items.

---

## 10. Box Recommendation

After creating an order, use:

```text
POST /api/orders/<order_id>/recommend-box/
```

No request body is required.

Example:

```text
POST /api/orders/2/recommend-box/
```

The system calculates the packing requirements and evaluates the available boxes.

---

## 11. Packing Approach

The system uses a **simplified deterministic greedy 3D packing heuristic**.

The approach is not intended to solve the general optimal 3D bin-packing problem.

### Packing Process

1. Order items are expanded according to their quantities.
2. Products are sorted approximately from larger to smaller volume.
3. Unique orientations of each product are considered.
4. Candidate positions are generated next to already packed products.
5. Each candidate placement is checked for overlap.
6. The placement that produces the smallest resulting bounding-box volume is selected.
7. The final bounding-box dimensions represent the estimated space required for the products.

Conceptually:

```text
Order
  │
  ├── Product A × 2
  ├── Product B × 1
  └── Product C × 1
          │
          ▼
   Expand quantities
          │
          ▼
   Consider orientations
          │
          ▼
   Place products using
   greedy 3D heuristic
          │
          ▼
   Calculate bounding box
          │
          ▼
   Required packed dimensions
```

---

## 12. Product Rotation

Product rotation is supported by considering different permutations of the product's length, width, and height.

For example, a product with:

```text
20 × 10 × 5
```

can be considered in orientations such as:

```text
20 × 10 × 5
20 × 5 × 10
10 × 20 × 5
10 × 5 × 20
5 × 20 × 10
5 × 10 × 20
```

Duplicate orientations are removed when dimensions are equal.

---

## 13. Box Eligibility

A box is considered eligible only when both hard constraints are satisfied.

### Dimension Constraint

The calculated packed dimensions must fit inside the box in at least one orientation.

```text
Packed dimensions ≤ Box dimensions
```

### Weight Constraint

The total weight of all products must not exceed the box's maximum weight capacity.

```text
Total order weight ≤ Box maximum weight
```

A box that fails either constraint is not considered for recommendation.

---

## 14. Box Selection Logic

Among all eligible boxes, the recommendation is ranked using:

1. **Lowest box cost**
2. **Lowest wasted volume**
3. **Lowest box ID**

### Wasted Volume

Wasted volume is calculated as:

```text
Wasted Volume =
Box Volume - Packed Bounding Volume
```

Where:

```text
Box Volume =
Box Length × Box Width × Box Height
```

and:

```text
Packed Bounding Volume =
Packed Length × Packed Width × Packed Height
```

For example:

```text
Box Volume = 30 × 20 × 15

Packed Volume = 20 × 15 × 10

Wasted Volume = 9000 - 3000
              = 6000
```

A box with lower cost is considered before wasted space. Wasted space is used as the second ranking criterion when costs are equal.

---

## 15. No Suitable Box

If none of the available boxes satisfies both the dimension and weight requirements, the API returns:

```json
{
    "order_id": 2,
    "recommended_box": null,
    "message": "No suitable box is available for this order."
}
```

The system does not select a box that violates the requirements.

---

## 16. Example Recommendation Response

A successful recommendation response has the following structure:

```json
{
    "order_id": 2,
    "recommended_box": {
        "id": 1,
        "name": "Medium Box",
        "length": "30.00",
        "width": "20.00",
        "height": "15.00",
        "max_weight": "10.00",
        "cost": "50.00"
    },
    "total_weight": "3.50",
    "packed_dimensions": {
        "length": "20.00",
        "width": "15.00",
        "height": "10.00"
    },
    "wasted_volume": "6000.00"
}
```

The values shown above are an example of the response structure. Actual values depend on the products, quantities, and boxes stored in the database.

---

## 17. Installation and Setup

### Prerequisites

Make sure Python is installed on your system.

### Clone the Repository

```bash
git clone <your-github-repository-url>
cd AI-Assisted-Box-Selection-System
```

### Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```text
DJANGO_SECRET_KEY=your-secret-key
```

Do not commit the `.env` file to GitHub.

### Apply Migrations

```bash
python manage.py migrate
```

### Create an Admin User

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## 18. Testing

The project uses Django's automated testing framework.

Run the complete test suite using:

```bash
python manage.py test
```

The current test suite contains **13 automated tests** covering:

- Order creation
- Order item quantities
- Total order weight
- Product packing
- Multiple product quantities
- Product rotation
- Box dimension validation
- Box weight validation
- Cost-based box selection
- Wasted-space comparison
- No suitable box
- Nested order API
- Box recommendation API

Detailed test cases are documented in:

`TEST_CASES.md`

The actual test execution output is documented in:

`TEST_OUTPUT.md`

---

## 19. Limitations

The packing implementation uses a simplified greedy heuristic rather than an exact 3D bin-packing optimization algorithm.

Therefore:

- The calculated packing arrangement is heuristic.
- It may not always produce the mathematically optimal arrangement.
- Candidate positions are generated using a limited set of positions adjacent to already packed products.
- The system currently recommends a single box for an order.
- Box inventory or physical stock tracking is outside the scope of this project.

---

## 20. Future Improvements

Possible future improvements include:

- More advanced 3D packing algorithms.
- Improved placement and search strategies.
- Support for multiple boxes for a single order.
- Performance optimization for very large orders.
- Additional API validation and authentication.
- A warehouse-friendly frontend interface.
- Integration with real warehouse box catalogues and order systems.

---

## 21. AI-Assisted Development

AI tools were used during development to assist with project planning, code development, debugging, testing, and documentation.

Details of the AI tools used, prompts, accepted and modified outputs, mistakes identified, and verification steps are documented separately in:

`AI_USAGE.md`

---

## 22. License

This project was developed as part of a technical assignment.