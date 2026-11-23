# Key Findings

This document separates figures verified directly from accessible source files from results displayed in the existing dashboard.

## 1. Dataset coverage

| Measure | Result | Verification |
|---|---:|---|
| Orders | 21,350 | Recalculated from orders.csv |
| Unique order IDs | 21,350 | Recalculated from orders.csv |
| Date range | 2015-01-01 to 2015-12-31 | Recalculated from orders.csv |
| Pizza-size products | 96 | Recalculated from pizzas.csv |
| Pizza types | 32 | Recalculated from pizza_types.csv |

The order file covers a full calendar year, which makes it possible to compare demand by date and time.

## 2. Order volume by hour

| Hour | Number of orders |
|---|---:|
| 12:00 | 2,520 |
| 13:00 | 2,455 |
| 18:00 | 2,399 |
| 17:00 | 2,336 |
| 19:00 | 2,009 |
| 16:00 | 1,920 |

### Interpretation

Noon is the busiest hour in the order table, followed by 13:00 and 18:00. The pattern suggests that lunch and early evening are important service periods. The business could use this as a starting point for staffing and preparation planning, then compare it with actual kitchen capacity and waiting-time data.

## 3. Dashboard sales indicators

The current Power BI dashboard displays:
- approximately $817.86K in total revenue;
- approximately 50K pizzas sold;
- approximately 21K orders;
- $38.31 average order value;
- The Classic Deluxe Pizza as the best-selling pizza by quantity; and
- The Thai Chicken Pizza as the highest-revenue pizza.

The dashboard also displays 30.03% quantity share for the Classic category and 45.89% revenue share for Large pizzas.

These are transcribed from the current dashboard/README, not independently recalculated in this review because the GitHub integration could not return the contents of order_details.csv. Run the included validation script locally to confirm exact totals before using them as exact figures in an interview or external report.

## 4. Business interpretation

The busiest hour is not necessarily the hour with the highest revenue or pizza quantity. Likewise, the most frequently ordered pizza is not necessarily the highest-revenue product. Keeping order count, quantity and revenue as separate measures gives the business a more useful picture.

The product-level results can help the restaurant monitor demand and plan availability. To make menu or pricing decisions, the business would need product costs, ingredient usage and customer feedback as well.

## 5. Recommended follow-up analysis

1. Compare quantity, revenue and average selling price for every pizza type.
2. Calculate category revenue and quantity shares using the underlying order lines.
3. Compare weekday and weekend demand.
4. Analyse average order size by hour and day.
5. Add ingredient and labour costs to calculate gross margin.
6. Add customer IDs to examine repeat orders and customer segments.
