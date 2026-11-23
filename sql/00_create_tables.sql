-- Pizza sales analysis: relational schema for the four source CSV files
-- MySQL 8.0+
CREATE DATABASE IF NOT EXISTS pizza_sales CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pizza_sales;

CREATE TABLE IF NOT EXISTS orders (
    order_id INT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    PRIMARY KEY (order_id),
    INDEX idx_orders_date (date),
    INDEX idx_orders_time (time)
);

CREATE TABLE IF NOT EXISTS pizza_types (
    pizza_type_id VARCHAR(50) NOT NULL,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    ingredients TEXT,
    PRIMARY KEY (pizza_type_id),
    INDEX idx_pizza_types_category (category)
);

CREATE TABLE IF NOT EXISTS pizzas (
    pizza_id VARCHAR(50) NOT NULL,
    pizza_type_id VARCHAR(50) NOT NULL,
    size VARCHAR(10) NOT NULL,
    price DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (pizza_id),
    CONSTRAINT fk_pizzas_type FOREIGN KEY (pizza_type_id) REFERENCES pizza_types(pizza_type_id),
    INDEX idx_pizzas_type_size (pizza_type_id, size)
);

CREATE TABLE IF NOT EXISTS order_details (
    order_details_id INT NOT NULL,
    order_id INT NOT NULL,
    pizza_id VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_details_id),
    CONSTRAINT fk_order_details_order FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_order_details_pizza FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id),
    INDEX idx_order_details_order (order_id),
    INDEX idx_order_details_pizza (pizza_id)
);

-- Import order: orders.csv, pizza_types.csv, pizzas.csv, order_details.csv
