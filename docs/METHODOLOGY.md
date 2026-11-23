# Analysis Methodology

## 1. Understand the source files

I began by reviewing the four CSV files and identifying what one row represented in each table. This was important because the order table and order-details table do not have the same level of detail.

- orders contains one row per order and its date/time.
- order_details contains the individual pizza lines and quantities.
- pizzas contains the size and listed price for each pizza product.
- pizza_types contains the product name, category and ingredients.

## 2. Map the relationships

I identified the keys connecting the tables:
- orders to order_details through order_id;
- order_details to pizzas through pizza_id; and
- pizzas to pizza_types through pizza_type_id.

This structure allows the analysis to combine order timing with product and price information without treating the four files as one flat table.

## 3. Check the data

I checked the accessible source tables for row counts, unique identifiers and date coverage. The orders file contains 21,350 unique orders between 1 January and 31 December 2015. The product catalogue contains 96 pizza-size combinations and 32 pizza types.

The order-details CSV is included in the repository, but the GitHub file reader could not return its contents during this review. The local validation script is therefore included so that the complete key checks and financial calculations can be run after cloning the repository.

## 4. Start with business-level KPIs

I used SQL aggregation to establish the number of orders and total revenue. Revenue is calculated as quantity multiplied by the listed price for the matching pizza. I also examined the highest listed price and the most frequently ordered size.

## 5. Explore product and category performance

I joined order_details to pizzas and pizza_types to compare quantity sold by pizza type and category. I then compared products by revenue as well as quantity. These measures answer different questions: quantity shows demand volume, while revenue also reflects price.

## 6. Analyse order timing

I used the time field to group orders by hour and identify busy periods. I also grouped pizza quantity by order date to calculate average daily volume. This helps describe when demand occurs, although it does not provide staffing or kitchen-capacity data by itself.

## 7. Use advanced SQL for deeper comparisons

For the advanced questions, I used:
- a CTE to calculate revenue by pizza type before calculating its share of total revenue;
- a window function to calculate cumulative revenue over time; and
- DENSE_RANK partitioned by category to rank pizzas within each category.

This made the analysis more reusable and avoided repeating the same aggregation in multiple places.

## 8. Present the results

I created two Power BI pages. The first is an executive overview of overall sales and order timing. The second focuses on product-level performance, allowing a viewer to compare products by revenue and quantity.

## 9. Interpret the findings responsibly

The data supports conclusions about order volume, listed-price revenue and product demand. It does not contain cost, discount, refund or customer data. For that reason, I describe sales performance rather than profitability, and I frame operational suggestions as areas for further investigation.
