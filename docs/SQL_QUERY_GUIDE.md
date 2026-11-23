# SQL Query Guide

The 13 original SQL files are numbered in the repository root. Run them against the four-table schema.

| File | Business question | Main SQL concepts |
|---|---|---|
| 01_total_orders.sql | How many distinct orders were placed? | COUNT DISTINCT |
| 02_total_revenue.sql | What is total sales revenue? | JOIN, SUM, multiplication |
| 03_highest_priced_pizza.sql | Which listed pizza-size product is most expensive? | JOIN, ORDER BY, LIMIT |
| 04_most_popular_pizza_size.sql | Which size sold the most units? | JOIN, GROUP BY, SUM |
| 05_top_5_pizza_types_by_quantity.sql | Which five pizza types sold the most units? | Multiple JOINs, GROUP BY |
| 06_category_wise_pizza_quantity.sql | How many units sold in each category? | JOIN, GROUP BY |
| 07_orders_by_hour.sql | When are orders placed? | HOUR, COUNT DISTINCT |
| 08_pizza_types_per_category.sql | How many pizza types are in each category? | COUNT DISTINCT |
| 09_average_daily_pizza_quantity.sql | What is average quantity sold per active order date? | Subquery, aggregation, AVG |
| 10_top_3_pizzas_by_revenue.sql | Which three pizza types generate the most revenue? | JOIN, SUM, ORDER BY |
| 11_revenue_contribution_percentage.sql | What share of revenue comes from each pizza type? | CTE, window SUM |
| 12_cumulative_revenue.sql | How does revenue accumulate over time? | CTE, SUM OVER |
| 13_top_3_pizzas_per_category.sql | Which three pizzas lead within each category? | CTE, DENSE_RANK, PARTITION BY |

## Calculation notes

**Revenue:** sum of order_details.quantity multiplied by the matching pizzas.price. This is sales value based on listed price, not profit.

**Average daily quantity:** the existing query calculates the average across dates that appear in the orders table. It represents average quantity per active sales day, not an average that includes calendar days with zero orders.

**Revenue contribution:** the query first calculates revenue by pizza type, then divides each product's revenue by total revenue using a window function.

**Top three within each category:** DENSE_RANK assigns a rank within each category. If multiple products tie at the third rank, the query can return more than three rows for that category. That is intentional tie-aware behaviour.

## Suggested improvements

- Include tie-handling rules explicitly when using LIMIT for ranked results.
- Compare both revenue and quantity when discussing product performance.
- Use date dimensions if the dashboard needs more advanced calendar comparisons.
- Keep revenue and profit terminology distinct.
