# Reproducing the Analysis

## Requirements

- MySQL 8.0 or a compatible MySQL server
- MySQL Workbench or another SQL client
- Microsoft Power BI Desktop
- Python 3.9+ for the optional CSV validation script

The Python validation script uses only the standard library; no pip packages are required.

## Step 1 — Get the project files

Clone the repository or download it as a ZIP. Keep the four CSV files together in the project directory.

## Step 2 — Create the database and tables

Open sql/00_create_tables.sql in MySQL Workbench and execute it. This creates the database and four tables with primary and foreign keys.

## Step 3 — Import the CSV files

Import each CSV into its matching table:
- orders.csv → orders
- pizza_types.csv → pizza_types
- pizzas.csv → pizzas
- order_details.csv → order_details

Import parent/reference tables before child tables if foreign-key checks are enabled. Confirm that the CSV header names match the table columns and that dates and times are imported using the expected formats.

## Step 4 — Run the SQL analysis

Run the numbered SQL files in the repository root in order. The SQL Query Guide explains each question and its SQL concepts.

## Step 5 — Validate the source files

From the repository root, run:

    python scripts/validate_data.py

The script checks required columns, blank values, duplicate keys, foreign-key matches and numeric fields. It recalculates order count, quantity sold and revenue using the CSV data. If the script reports a problem, investigate it before relying on dashboard figures.

## Step 6 — Open the Power BI dashboard

Open A1pizzashop_analytics_dashboard.pbix in Power BI Desktop. If prompted, update the source paths to the local CSV files and refresh the model.

Compare the dashboard's headline values with the results from MySQL and the validation script.

## Reproducibility caveats

- The PBIX may contain local file paths from the original machine. Update those paths after downloading the repository.
- The SQL schema file creates the database tables but does not automatically import the CSVs; import them through Workbench or use an appropriate local bulk-load process.
- The original dataset source and redistribution terms still need to be confirmed and credited.
