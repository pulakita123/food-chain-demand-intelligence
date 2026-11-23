#!/usr/bin/env python3
"""Validate Pizza Sales CSV files and recalculate core KPIs using stdlib only."""
from __future__ import annotations
import csv
from collections import Counter
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read_csv(filename):
    path = ROOT / filename
    if not path.exists():
        raise FileNotFoundError("Missing required file: " + filename)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def require_columns(rows, filename, columns):
    if not rows:
        raise ValueError(filename + " has no data rows.")
    missing = columns - set(rows[0])
    if missing:
        raise ValueError(filename + " is missing columns: " + str(sorted(missing)))

def duplicates(values):
    return len(values) - len(set(values))

def main():
    orders = read_csv("orders.csv")
    details = read_csv("order_details.csv")
    pizzas = read_csv("pizzas.csv")
    types = read_csv("pizza_types.csv")

    require_columns(orders, "orders.csv", {"order_id", "date", "time"})
    require_columns(details, "order_details.csv", {"order_details_id", "order_id", "pizza_id", "quantity"})
    require_columns(pizzas, "pizzas.csv", {"pizza_id", "pizza_type_id", "size", "price"})
    require_columns(types, "pizza_types.csv", {"pizza_type_id", "name", "category", "ingredients"})

    order_ids = [r["order_id"].strip() for r in orders]
    line_ids = [r["order_details_id"].strip() for r in details]
    pizza_ids = [r["pizza_id"].strip() for r in pizzas]
    type_ids = [r["pizza_type_id"].strip() for r in types]
    order_set, pizza_set, type_set = set(order_ids), set(pizza_ids), set(type_ids)

    dates = [date.fromisoformat(r["date"].strip()) for r in orders]
    hours = Counter(datetime.strptime(r["time"].strip(), "%H:%M:%S").hour for r in orders)

    blank_cells = 0
    required = [
        (orders, {"order_id", "date", "time"}),
        (details, {"order_details_id", "order_id", "pizza_id", "quantity"}),
        (pizzas, {"pizza_id", "pizza_type_id", "size", "price"}),
        (types, {"pizza_type_id", "name", "category"}),
    ]
    for rows, columns in required:
        blank_cells += sum(1 for row in rows for col in columns if not (row.get(col) or "").strip())

    orphan_orders = sum(1 for r in details if r["order_id"].strip() not in order_set)
    orphan_pizzas = sum(1 for r in details if r["pizza_id"].strip() not in pizza_set)
    orphan_types = sum(1 for r in pizzas if r["pizza_type_id"].strip() not in type_set)

    price_map = {r["pizza_id"].strip(): Decimal(r["price"]) for r in pizzas}
    quantity_total, revenue = 0, Decimal("0")
    invalid_quantities = 0
    for row in details:
        qty = int(row["quantity"])
        if qty <= 0:
            invalid_quantities += 1
        quantity_total += qty
        pizza_id = row["pizza_id"].strip()
        if pizza_id not in price_map:
            raise ValueError("Unknown pizza_id in order_details: " + pizza_id)
        revenue += Decimal(qty) * price_map[pizza_id]

    order_count = len(order_set)
    aov = revenue / order_count if order_count else Decimal("0")
    avg_pizzas = Decimal(quantity_total) / order_count if order_count else Decimal("0")

    print("DATASET PROFILE")
    print("Orders: {} rows / {} unique IDs".format(len(orders), order_count))
    print("Order-detail rows: {}".format(len(details)))
    print("Pizza-size products: {}".format(len(pizzas)))
    print("Pizza types: {}".format(len(types)))
    print("Date range: {} to {}".format(min(dates), max(dates)))
    busiest = hours.most_common(1)[0]
    print("Busiest order hour: {:02d}:00 ({} orders)".format(busiest[0], busiest[1]))

    print("\nDATA QUALITY")
    print("Blank required cells: {}".format(blank_cells))
    print("Duplicate order IDs: {}".format(duplicates(order_ids)))
    print("Duplicate order-detail IDs: {}".format(duplicates(line_ids)))
    print("Duplicate pizza IDs: {}".format(duplicates(pizza_ids)))
    print("Duplicate pizza-type IDs: {}".format(duplicates(type_ids)))
    print("Orphan order references: {}".format(orphan_orders))
    print("Orphan pizza references: {}".format(orphan_pizzas))
    print("Orphan pizza-type references: {}".format(orphan_types))
    print("Non-positive quantity rows: {}".format(invalid_quantities))

    print("\nRECALCULATED KPIs")
    print("Orders: {:,}".format(order_count))
    print("Pizzas sold: {:,}".format(quantity_total))
    print("Revenue: USD {:,.2f}".format(revenue))
    print("Average order value: USD {:,.2f}".format(aov))
    print("Average pizzas per order: {:.2f}".format(avg_pizzas))

    problems = []
    if blank_cells:
        problems.append("blank required cells were found")
    if any([duplicates(order_ids), duplicates(line_ids), duplicates(pizza_ids), duplicates(type_ids)]):
        problems.append("duplicate primary keys were found")
    if any([orphan_orders, orphan_pizzas, orphan_types]):
        problems.append("orphan foreign-key references were found")
    if invalid_quantities:
        problems.append("non-positive quantities were found")

    if problems:
        print("\nVALIDATION: REVIEW REQUIRED")
        for problem in problems:
            print("- " + problem)
        return 1
    print("\nVALIDATION: PASSED")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
