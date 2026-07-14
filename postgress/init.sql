CREATE TABLE IF NOT EXISTS gold_sales_by_date (
    order_date DATE PRIMARY KEY,
    total_sales NUMERIC(18, 2),
    total_profit NUMERIC(18, 2),
    total_quantity INT
);

CREATE TABLE IF NOT EXISTS gold_sales_by_category (
    category VARCHAR(255) PRIMARY KEY,
    total_sales NUMERIC(18, 2),
    total_profit NUMERIC(18, 2),
    total_quantity INT
);