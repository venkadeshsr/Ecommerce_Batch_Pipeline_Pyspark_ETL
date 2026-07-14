CREATE TABLE IF NOT EXISTS silver_orders (
    order_date DATE,
    product_name VARCHAR(255),
    category VARCHAR(255),
    region VARCHAR(255),
    quantity INT,
    sales NUMERIC(12, 2),
    profit NUMERIC(12, 2),
    year INT,
    month INT,
    quarter INT,
    profit_margin NUMERIC(12, 2)
);

CREATE TABLE IF NOT EXISTS gold_sales_by_date (
    order_date DATE,
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_sales_by_product (
    product_name VARCHAR(255),
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_sales_by_category (
    category VARCHAR(255),
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_sales_by_region (
    region VARCHAR(255),
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_monthly_sales (
    year INT,
    month INT,
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_product_region (
    product_name VARCHAR(255),
    region VARCHAR(255),
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_category_region (
    category VARCHAR(255),
    region VARCHAR(255),
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);

CREATE TABLE IF NOT EXISTS gold_kpi_summary (
    total_sales NUMERIC(12, 2),
    total_profit NUMERIC(12, 2),
    total_quantity BIGINT
);