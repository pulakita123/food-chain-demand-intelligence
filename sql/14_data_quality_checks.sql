-- Data-quality checks for the Pizza Sales Analysis database
USE pizza_sales;

-- Table row counts
SELECT 'orders' AS table_name, COUNT(*) AS row_count FROM orders
UNION ALL SELECT 'order_details', COUNT(*) FROM order_details
UNION ALL SELECT 'pizzas', COUNT(*) FROM pizzas
UNION ALL SELECT 'pizza_types', COUNT(*) FROM pizza_types;

-- Duplicate primary-key checks (each should return zero rows)
SELECT order_id, COUNT(*) AS occurrences FROM orders GROUP BY order_id HAVING COUNT(*) > 1;
SELECT order_details_id, COUNT(*) AS occurrences FROM order_details GROUP BY order_details_id HAVING COUNT(*) > 1;
SELECT pizza_id, COUNT(*) AS occurrences FROM pizzas GROUP BY pizza_id HAVING COUNT(*) > 1;
SELECT pizza_type_id, COUNT(*) AS occurrences FROM pizza_types GROUP BY pizza_type_id HAVING COUNT(*) > 1;

-- Orphan relationships (each should return zero rows)
SELECT od.order_id FROM order_details od LEFT JOIN orders o ON o.order_id = od.order_id WHERE o.order_id IS NULL;
SELECT od.pizza_id FROM order_details od LEFT JOIN pizzas p ON p.pizza_id = od.pizza_id WHERE p.pizza_id IS NULL;
SELECT p.pizza_type_id FROM pizzas p LEFT JOIN pizza_types pt ON pt.pizza_type_id = p.pizza_type_id WHERE pt.pizza_type_id IS NULL;

-- Invalid numeric values
SELECT * FROM order_details WHERE quantity <= 0;
SELECT * FROM pizzas WHERE price < 0;

-- Date coverage and busiest hours
SELECT MIN(date) AS first_order_date, MAX(date) AS last_order_date, COUNT(DISTINCT date) AS active_order_days FROM orders;
SELECT HOUR(time) AS order_hour, COUNT(DISTINCT order_id) AS order_count FROM orders GROUP BY HOUR(time) ORDER BY order_hour;

-- Recalculate core KPIs
SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(od.quantity) AS pizzas_sold,
    ROUND(SUM(od.quantity * p.price), 2) AS total_revenue,
    ROUND(SUM(od.quantity * p.price) / COUNT(DISTINCT o.order_id), 2) AS average_order_value,
    ROUND(SUM(od.quantity) / COUNT(DISTINCT o.order_id), 2) AS average_pizzas_per_order
FROM orders o
JOIN order_details od ON od.order_id = o.order_id
JOIN pizzas p ON p.pizza_id = od.pizza_id;
