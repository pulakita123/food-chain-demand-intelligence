# Food Chain Demand Intelligence | MySQL & Power BI

I built this project to understand what drives sales in a pizza business: which products customers order, when demand is highest, and how different pizza types, sizes and categories contribute to revenue.

I used MySQL for the relational data analysis and Power BI to present the results in a two-page interactive dashboard. The work is organised around business questions rather than a list of SQL functions, so a reviewer can follow the problem, analysis, findings and possible business actions.

[Open the Power BI dashboard](./A1pizzashop_analytics_dashboard.pbix) · [Read the project report](./Pizza_Sales_Project_Report.docx)

## Project snapshot

| Item | Detail |
|---|---|
| Project type | Sales and business performance analysis |
| Tools | MySQL 8, MySQL Workbench, Power BI |
| Period | 1 January–31 December 2015 |
| Orders | 21,350 unique orders, verified from orders.csv |
| Product catalogue | 32 pizza types and 96 size/product combinations |
| Deliverables | 13 SQL analyses, Power BI dashboard, project report |

The current dashboard displays approximately **$817.86K revenue**, **50K pizzas sold**, **21K orders** and an **average order value of $38.31**. The 50K and 21K values are rounded dashboard displays. Exact totals should be checked by running the SQL and validation script included in this repository.

## The business problem

A restaurant may know its total sales, but that number alone does not explain what is driving performance. The team also needs to understand which products customers choose, which sizes and categories contribute most, and when demand is highest.

I approached the data as if I were supporting a pizza shop's sales manager. I wanted to move beyond reporting totals and answer questions that could support product planning, promotions, staffing and inventory decisions.

### Questions I wanted to answer

1. How many orders did the shop receive, and how much revenue did it generate?
2. Which pizza types and sizes are ordered most often?
3. Which products generate the highest revenue?
4. How does demand differ across pizza categories?
5. At what times of day does the shop receive the most orders?
6. How do daily sales patterns change over the year?
7. What percentage of revenue comes from each pizza type?
8. Which pizzas perform best within each category?

## Dashboard preview

### Page 1 — Executive Sales Overview

<img width="578" alt="Executive sales overview dashboard" src="https://github.com/user-attachments/assets/9b3945ec-17a4-4bd8-ae09-4ab6021412b2" />

This page gives a quick view of revenue, pizzas sold, orders, average order value and average pizzas per order. It also lets the viewer explore demand by size, category, hour and date.

### Page 2 — Product and Sales Performance

<img width="574" alt="Product and sales performance dashboard" src="https://github.com/user-attachments/assets/c11e4eda-e551-40e2-b1ec-0dfd96945128" />

This page focuses on individual pizza types and compares products by revenue and quantity. This makes it easier to distinguish popular products from products that generate higher sales value.

## Key findings

The points below separate checks made directly on accessible CSV files from results shown in the existing dashboard.

### 1. The shop processed 21,350 orders during 2015

I checked orders.csv directly. It contains 21,350 rows and 21,350 distinct order IDs, covering 1 January to 31 December 2015.

### 2. Noon is the busiest order hour

I grouped the order timestamps by hour. 12:00 noon was the busiest hour, with 2,520 orders. 13:00 followed with 2,455 orders, and 18:00 recorded 2,399 orders.

This is useful for planning staff coverage and preparation capacity. It does not, by itself, tell us how many pizzas were prepared at each hour, because an order can contain multiple pizzas.

### 3. The leading product depends on the measure

The dashboard identifies The Classic Deluxe Pizza as the best-selling pizza by quantity and The Thai Chicken Pizza as the highest-revenue pizza. A product can be ordered frequently without generating the highest sales value.

### 4. Size and category mix matter

The existing dashboard reports that Large pizzas contribute 45.89% of revenue and that the Classic category accounts for 30.03% of pizza quantity sold. These comparisons help describe the product mix and should be reviewed alongside both revenue and quantity.

## How I approached the analysis

I started by understanding the four CSV files rather than immediately writing queries. The order table records when each order was placed. The order-details table records the pizzas and quantities included in each order. The pizzas table provides size and price information, while the pizza-types table contains product names, categories and ingredients.

After mapping the relationships, I used SQL joins to bring the relevant information together. I began with basic KPIs such as order count and revenue, then moved to product and category comparisons. I examined hourly demand and average daily quantity, and used CTEs and window functions for revenue contribution, cumulative revenue and ranking products within each category.

I then used Power BI to present the results in two views: an executive overview and a product-performance page.

See [Methodology](docs/METHODOLOGY.md) for the full workflow and [Data Dictionary](docs/DATA_DICTIONARY.md) for the table definitions and relationships.

## SQL analysis

The 13 original SQL files are numbered 01 to 13 in the repository root. They progress from basic aggregation to advanced analysis.

| Level | Analysis | SQL concepts |
|---|---|---|
| Basic | Order count, revenue, highest-priced product, popular size, top five pizzas by quantity | Aggregation, joins, GROUP BY, ORDER BY, LIMIT |
| Intermediate | Quantity by category, orders by hour, product count by category, average daily quantity | Date/time functions, subqueries |
| Advanced | Top pizzas by revenue, revenue contribution, cumulative revenue, top three within category | CTEs, window functions, DENSE_RANK |

Start with [01_total_orders.sql](01_total_orders.sql). The [SQL Query Guide](docs/SQL_QUERY_GUIDE.md) explains each query and the business question it answers.

## Business recommendations

1. **Plan service coverage around busy periods.** The order timestamps show strong lunchtime and evening demand. Compare this with staffing rosters, preparation times and queue lengths before changing shifts.
2. **Protect availability of popular products.** The Classic Deluxe leads by quantity in the dashboard. Monitor its ingredient availability and stock levels.
3. **Review quantity and revenue together.** The Thai Chicken leads the dashboard's revenue comparison, while the Classic Deluxe leads by quantity.
4. **Use category and size mix for inventory planning.** These breakdowns can help the team understand the product mix and prepare ingredients accordingly.
5. **Investigate weaker products before changing the menu.** Low revenue alone is not enough reason to discontinue a product. Review margin, ingredient cost, preparation time and customer feedback as well.

These are follow-up recommendations, not claims that the dataset proves a particular cause or financial outcome.

## Repository structure

```text
food-chain-demand-intelligence/
├── README.md
├── 01_total_orders.sql
├── 02_total_revenue.sql
├── ... (13 numbered SQL analysis files)
├── orders.csv
├── order_details.csv
├── pizzas.csv
├── pizza_types.csv
├── A1pizzashop_analytics_dashboard.pbix
├── Pizza_Sales_Project_Report.docx
├── Screenshot 2026-11-15 003335.png
├── Screenshot 2026-11-15 003442.png
├── Screenshot 2026-11-15 013117.png
├── sql/
│   ├── 00_create_tables.sql
│   └── 14_data_quality_checks.sql
├── scripts/
│   └── validate_data.py
├── docs/
│   ├── BUSINESS_PROBLEM.md
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   ├── KEY_FINDINGS.md
│   ├── SQL_QUERY_GUIDE.md
│   ├── RECOMMENDATIONS_AND_LIMITATIONS.md
│   └── REPRODUCING_ANALYSIS.md
└── .gitignore
```

## How to reproduce the project

1. Clone or download this repository.
2. Create the database and tables using [sql/00_create_tables.sql](sql/00_create_tables.sql).
3. Import the four CSV files into their matching tables. Import parent tables before dependent tables if foreign-key constraints are enabled.
4. Run the numbered SQL files in order in MySQL Workbench.
5. Run [scripts/validate_data.py](scripts/validate_data.py) from the repository root to check the CSV files and recalculate core totals.
6. Open the PBIX file in Power BI Desktop. If prompted, update the CSV source paths and refresh the model.
7. Compare dashboard headline cards with the SQL and Python validation results.

See [Reproducing the Analysis](docs/REPRODUCING_ANALYSIS.md) for detailed setup steps.

## Skills demonstrated

- Relational data analysis and SQL joins
- Aggregations, subqueries and CTEs
- Window functions and ranking
- Date/time analysis
- KPI definition and business interpretation
- Power BI dashboard design and data visualisation
- Translating findings into operational questions and recommendations

## Limitations and next steps

The data covers orders, products, sizes, prices, categories and ingredients. It does not include ingredient costs, labour costs, delivery costs, discounts, refunds, customer demographics or customer satisfaction. This project therefore analyses sales and demand, not profit or customer lifetime value.

If I were extending the analysis, I would add product costs and discounts to calculate gross margin, include customer identifiers to study repeat purchasing, and combine order patterns with inventory and staffing data.

## About this project

I built this project to practise taking a business question through the full analysis process: understanding the data, querying related tables, checking patterns, building a dashboard and explaining what the results could mean to a business team.

---

**Project area:** Data Analytics | **Tools:** MySQL, Power BI | **Focus:** Sales performance, product analysis and business insights

*Dataset attribution: the original source and redistribution terms for the four CSV files have not yet been confirmed. Add the original dataset creator/source and applicable licence before redistributing the data.*
