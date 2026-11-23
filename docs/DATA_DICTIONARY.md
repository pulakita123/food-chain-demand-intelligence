# Data Dictionary

The project uses four CSV files that form a small relational model.

## orders.csv

One row represents one customer order.

| Column | Meaning | Type |
|---|---|---|
| order_id | Unique order identifier | Integer / primary key |
| date | Date the order was placed | Date (YYYY-MM-DD) |
| time | Time the order was placed | Time (HH:MM:SS) |

## order_details.csv

One row represents one pizza line within an order. An order can contain multiple rows.

| Column | Meaning | Type |
|---|---|---|
| order_details_id | Unique order-line identifier | Integer / primary key |
| order_id | Order containing this line | Integer / foreign key to orders |
| pizza_id | Pizza-size product ordered | Text / foreign key to pizzas |
| quantity | Number of units on this line | Integer |

## pizzas.csv

One row represents a specific pizza type and size.

| Column | Meaning | Type |
|---|---|---|
| pizza_id | Unique pizza-size identifier | Text / primary key |
| pizza_type_id | Product type identifier | Text / foreign key to pizza_types |
| size | Size variant (S, M, L, XL, XXL where available) | Text |
| price | Listed selling price per pizza | Decimal |

## pizza_types.csv

One row represents a named pizza type.

| Column | Meaning | Type |
|---|---|---|
| pizza_type_id | Unique pizza type identifier | Text / primary key |
| name | Display name of the pizza | Text |
| category | Product category | Text |
| ingredients | Ingredient description | Text |

## Relationships

    orders (1) ───── (*) order_details (*) ───── (1) pizzas (*) ───── (1) pizza_types
     order_id                order_id               pizza_id             pizza_type_id

The intended joins are:
- orders.order_id = order_details.order_id
- order_details.pizza_id = pizzas.pizza_id
- pizzas.pizza_type_id = pizza_types.pizza_type_id

## Data observations verified from accessible files

- orders.csv contains 21,350 rows and 21,350 distinct order IDs.
- The order date range is 2015-01-01 through 2015-12-31.
- pizzas.csv contains 96 product-size rows.
- pizza_types.csv contains 32 pizza types.
- No duplicate order IDs were found in the accessible order file.
- No duplicate pizza IDs or pizza type IDs were found in the two accessible product files.

The order_details.csv file is present in the repository, but its contents could not be read through the GitHub integration during this review. Run the validation script locally to check its row count, key integrity and numeric fields.

## Important definitions

- **Order:** a distinct order_id in orders.
- **Order line:** one row in order_details.
- **Pizzas sold:** sum of order_details.quantity.
- **Revenue:** sum of quantity multiplied by the matching pizza price.
- **Average order value:** revenue divided by distinct orders.
- **Average pizzas per order:** total quantity divided by distinct orders.

Revenue is sales value based on the listed price in pizzas.csv. It should not be called profit because product costs and operating expenses are not included.
