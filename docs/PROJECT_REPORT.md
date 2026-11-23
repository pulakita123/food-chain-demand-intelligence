# Project Report: Food Chain Demand Intelligence

## 1. Introduction

For this project, I wanted to understand demand patterns in a food-service business. Rather than looking only at total sales, I wanted to know which products customers order, when orders are most frequent and how different product categories contribute to sales.

The project uses a pizza restaurant dataset as a focused case study. The portfolio title is Food Chain Demand Intelligence, but the available data represents one restaurant rather than a multi-outlet chain.

## 2. Business problem

The business question guiding the analysis was:

**How can order and product data help a restaurant understand demand, product performance and busy service periods?**

I focused on order volume, revenue, product popularity, category and size mix, hourly demand and daily patterns. These questions can support further discussion around staffing, preparation capacity, menu planning and inventory.

## 3. Understanding the data

The project contains four related CSV files:

- `orders.csv` records when each order was placed.
- `order_details.csv` records the pizzas and quantities included in each order.
- `pizzas.csv` contains pizza size and price information.
- `pizza_types.csv` contains product names, categories and ingredients.

I used the relationships between these tables to connect order activity with product information. This allowed me to analyse both the timing of orders and the products included in them.

## 4. Analysis approach

I used MySQL to answer business questions through joins, aggregations, subqueries, CTEs and window functions. I started with basic measures such as order count and revenue, then moved to product and category comparisons.

I also grouped orders by hour to identify busy periods. For more advanced questions, I used ranking and cumulative calculations to compare products and their contribution.

Power BI was used to present the analysis through an executive sales overview and a product-performance dashboard.

## 5. Key findings

The orders table contains 21,350 distinct orders across 1 January to 31 December 2015. The product catalogue contains 32 pizza types and 96 size/product combinations.

The busiest hour was 12:00 noon, with 2,520 orders. This was followed by 13:00 with 2,455 orders and 18:00 with 2,399 orders. This points to lunchtime and early evening as important service periods, although order count alone does not measure kitchen workload because an order may contain multiple pizzas.

The dashboard identifies The Classic Deluxe Pizza as the leading product by quantity and The Thai Chicken Pizza as the leading product by revenue. This distinction matters: the most frequently ordered product is not necessarily the one generating the highest sales value.

The dashboard also shows that Large pizzas account for 45.89% of revenue and the Classic category accounts for 30.03% of quantity sold. These are dashboard-displayed values and should be cross-checked against a refreshed report and the source data before being quoted as independently verified totals.

## 6. Business recommendations

Based on the patterns, I would suggest:

1. Review staffing and preparation coverage around lunchtime and early evening, using waiting-time and kitchen-capacity data before changing shifts.
2. Monitor availability of popular products such as The Classic Deluxe.
3. Review quantity and revenue together when evaluating menu performance.
4. Use category and size mix to support ingredient planning.
5. Investigate product costs, preparation time and customer feedback before considering menu changes.

These are practical follow-up ideas. The dataset does not contain the cost, staffing or customer feedback information needed to measure the impact of these actions.

## 7. Limitations

The available data supports sales and demand analysis. It does not include ingredient costs, labour costs, delivery expenses, discounts, refunds, customer demographics or customer satisfaction. Therefore, this project does not claim to measure profit, customer lifetime value or the performance of a multi-location food chain.

The original dataset source and redistribution terms also need to be confirmed and credited.

## 8. What I would do next

I would extend the analysis with ingredient costs and labour information to estimate product margins and service capacity. Customer identifiers would make it possible to examine repeat ordering, while inventory data could help connect demand patterns with stock availability.

## 9. Conclusion

This project gave me practice in taking a business question through relational data analysis, SQL querying, dashboard development and business interpretation. The main takeaway is that order volume, product quantity and revenue each reveal a different part of demand. Reviewing them together gives a more useful basis for operational questions than looking at total sales alone.

---

*This is an independent portfolio case study based on a single pizza restaurant dataset. Findings are descriptive and should be interpreted within the limits of the available fields.*