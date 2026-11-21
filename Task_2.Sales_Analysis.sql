CREATE database Sales_Analysis;
USE Sales_Analysis;

-- 1. Create Customers Table
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_segment VARCHAR(20),
    signup_year INT,
    city VARCHAR(50)
);

-- 2. Create Sales Data Table
CREATE TABLE sales_data (
    order_id VARCHAR(10) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(10),
    customer_name VARCHAR(50),
    region VARCHAR(20),
    product_category VARCHAR(30),
    product_name VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10, 2),
    discount DECIMAL(4, 2),
    marketing_spend DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 3. Insert Customers Data
INSERT INTO customers VALUES
('CUST-01', 'Corporate', 2023, 'Delhi'),
('CUST-02', 'Consumer', 2024, 'Mumbai'),
('CUST-03', 'Home Office', 2023, 'Bengaluru'),
('CUST-04', 'Consumer', 2025, 'Kolkata'),
('CUST-05', 'Corporate', 2022, 'Jaipur'),
('CUST-06', 'Consumer', 2024, 'Pune'),
('CUST-07', 'Home Office', 2025, 'Chennai'),
('CUST-08', 'Corporate', 2023, 'Bhubaneswar'),
('CUST-09', 'Consumer', 2025, 'Lucknow'),
('CUST-10', 'Home Office', 2024, 'Ahmedabad'),
('CUST-11', 'Consumer', 2025, 'Hyderabad'),
('CUST-12', 'Corporate', 2022, 'Patna');

-- 4. Insert Cleaned Sales Data
INSERT INTO sales_data VALUES
('ORD-1001', '2026-01-05', 'CUST-01', 'Aarav Sharma', 'North', 'Electronics', 'Wireless Mouse', 2, 800, 0.05, 150),
('ORD-1002', '2026-01-07', 'CUST-02', 'Priya Patel', 'West', 'Furniture', 'Office Chair', 1, 7500, 0.10, 500),
('ORD-1003', '2026-01-08', 'CUST-03', 'Rohan Verma', 'South', 'Electronics', 'Mechanical Keyboard', 1, 3200, 0.00, 200),
('ORD-1004', '2026-01-10', 'CUST-01', 'Aarav Sharma', 'North', 'Office Supplies', 'A4 Paper Rim', 5, 300, 0.00, 50),
('ORD-1005', '2026-01-12', 'CUST-04', 'Sneha Gupta', 'East', 'Electronics', 'USB-C Hub', 3, 1200, 0.05, 180),
('ORD-1006', '2026-01-15', 'CUST-05', 'Vikram Singh', 'North', 'Furniture', 'Study Desk', 1, 12000, 0.15, 800),
('ORD-1007', '2026-01-18', 'CUST-06', 'Ananya Roy', 'West', 'Office Supplies', 'Gel Pen Box', 10, 150, 0.00, 60),
('ORD-1008', '2026-01-20', 'CUST-02', 'Priya Patel', 'West', 'Electronics', '27-inch Monitor', 1, 18500, 0.10, 1100),
('ORD-1009', '2026-01-22', 'CUST-07', 'Kabir Das', 'South', 'Furniture', 'Bookshelf', 2, 4500, 0.05, 400),
('ORD-1010', '2026-01-25', 'CUST-08', 'Meera Nair', 'East', 'Electronics', 'Unknown Product', 1, 2500, 0.00, 150),
('ORD-1011', '2026-01-28', 'CUST-09', 'Arjun Mehta', 'North', 'Office Supplies', 'Whiteboard', 2, 1800, 0.05, 120),
('ORD-1012', '2026-02-02', 'CUST-03', 'Rohan Verma', 'South', 'Electronics', 'Noise Cancelling Headphones', 1, 9500, 0.10, 650),
('ORD-1013', '2026-02-04', 'CUST-10', 'Diya Kapoor', 'West', 'Furniture', 'Ergonomic Footrest', 4, 1500, 0.00, 220),
('ORD-1014', '2026-02-06', 'CUST-01', 'Aarav Sharma', 'North', 'Electronics', 'Webcam HD', 2, 2800, 0.05, 250),
('ORD-1015', '2026-02-09', 'CUST-05', 'Vikram Singh', 'North', 'Office Supplies', 'Printer Ink', 50, 900, 0.20, 1500),
('ORD-1016', '2026-02-11', 'CUST-11', 'Neha Joshi', 'South', 'Electronics', 'Laptop Stand', 3, 1100, 0.00, 140),
('ORD-1017', '2026-02-14', 'CUST-06', 'Ananya Roy', 'West', 'Furniture', 'Desk Lamp', 2, 1400, 0.05, 110),
('ORD-1018', '2026-02-16', 'CUST-12', 'Karan Malhotra', 'East', 'Office Supplies', 'Notebook Pack', 6, 400, 0.00, 80),
('ORD-1019', '2026-02-19', 'CUST-08', 'Meera Nair', 'East', 'Electronics', 'External SSD 1TB', 1, 8200, 0.10, 550),
('ORD-1020', '2026-02-22', 'CUST-04', 'Sneha Gupta', 'East', 'Furniture', 'Mesh Backrest', 2, 1600, 0.05, 160);

-- 5. Basic filtering and sorting
SELECT 
    order_id,
    order_date,
    customer_name,
    product_name,
    quantity,
    unit_price,
    ROUND(quantity * unit_price * (1 - discount), 2) AS net_revenue
FROM sales_data
WHERE product_category = 'Electronics' 
  AND unit_price > 3000
ORDER BY net_revenue DESC;

-- 6. Aggregation and Grouping
SELECT 
    product_category,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS total_revenue,
    ROUND(AVG(quantity * unit_price * (1 - discount)), 2) AS avg_order_value
FROM sales_data
GROUP BY product_category
HAVING SUM(quantity * unit_price * (1 - discount)) > 25000
ORDER BY total_revenue DESC;

-- 7. Combining Tables
SELECT 
    c.customer_segment,
    c.city,
    COUNT(s.order_id) AS order_count,
    ROUND(SUM(s.quantity * s.unit_price * (1 - s.discount)), 2) AS segment_revenue
FROM sales_data s
INNER JOIN customers c 
    ON s.customer_id = c.customer_id
GROUP BY c.customer_segment, c.city
ORDER BY segment_revenue DESC;

-- 8. Filtering and Subqueries
SELECT 
    order_id,
    customer_name,
    product_name,
    ROUND(quantity * unit_price * (1 - discount), 2) AS net_revenue
FROM sales_data
WHERE (quantity * unit_price * (1 - discount)) > (
    SELECT AVG(quantity * unit_price * (1 - discount)) 
    FROM sales_data
)
ORDER BY net_revenue DESC;

-- 9. Ranking and Running Totals
-- Query A: Rank customers by total revenue within each region
SELECT 
    region,
    customer_name,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS total_spent,
    RANK() OVER (
        PARTITION BY region 
        ORDER BY SUM(quantity * unit_price * (1 - discount)) DESC
    ) AS regional_rank
FROM sales_data
GROUP BY region, customer_name;

-- Query B: Calculate cumulative (running) revenue by order date
SELECT 
    order_id,
    order_date,
    ROUND(quantity * unit_price * (1 - discount), 2) AS order_revenue,
    ROUND(SUM(quantity * unit_price * (1 - discount)) OVER (
        ORDER BY order_date, order_id
    ), 2) AS running_total_revenue
FROM sales_data;

