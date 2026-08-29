-- =====================================
-- CUSTOMER ANALYSIS
-- =====================================
USE ecommerce_project;

-- Revenue by loyalty tier
SELECT
u.loyalty_tier,
SUM(p.total_amount) AS revenue
FROM purchases p
JOIN users u
	ON p.user_id = u.user_id
GROUP BY u.loyalty_tier
ORDER BY revenue DESC;

-- Revenue by Income level
SELECT
u.income_level,
SUM(p.total_amount) AS revenue
FROM purchases p
JOIN users u
	ON p.user_id = u.user_id
GROUP BY u.income_level
ORDER BY revenue DESC;

-- Revenue by Country
SELECT
u.country,
SUM(p.total_amount) AS revenue
FROM purchases p
JOIN users u
	ON p.user_id = u.user_id
GROUP BY u.country
ORDER BY revenue DESC;

-- Average Order Value by Country
SELECT
u.country,
AVG(p.total_amount) AS avg_order_value
FROM purchases p
JOIN users u
	ON p.user_id = u.user_id
GROUP BY u.country
ORDER BY avg_order_value DESC;

-- Revenue by category
SELECT
pr.category,
SUM(p.total_amount) AS revenue
FROM purchases p
JOIN products pr
	ON p.product_id = pr.product_id
GROUP BY pr.category
ORDER BY revenue DESC;

-- Revenue by brand
SELECT
pr.brand,
SUM(p.total_amount) AS revenue
FROM purchases p
JOIN products pr
	ON p.product_id = pr.product_id
GROUP BY pr.brand
ORDER BY revenue DESC;

-- Average price by category
SELECT
category,
AVG(price) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- Top 10 products by Revenue
SELECT
pr.product_name,
SUM(p.total_amount) AS revenue
FROM purchases p
JOIN products pr
	ON p.product_id = pr.product_id
GROUP BY pr.product_name
ORDER BY revenue DESC
LIMIT 10;

-- Top 10 products by Quantity sold
SELECT
pr.product_name,
SUM(p.quantity) AS units_sold
FROM purchases p
JOIN products pr
	ON p.product_id = pr.product_id
GROUP BY pr.product_name
ORDER BY units_sold DESC
LIMIT 10;

-- Average rating by category
SELECT
pr.category,
AVG(r.rating) AS avg_rating
FROM reviews r
JOIN products pr
	ON r.product_id = pr.product_id
GROUP BY pr.category
ORDER BY avg_rating DESC;

-- Average rating by brand
SELECT
pr.brand,
AVG(r.rating) AS avg_rating
FROM reviews r
JOIN products pr
	ON r.product_id = pr.product_id
GROUP BY pr.brand
ORDER BY avg_rating DESC;

-- Number of reviews by brand
SELECT
pr.brand,
COUNT(*) AS review_count
FROM reviews r
JOIN products pr
	ON r.product_id = pr.product_id
GROUP BY pr.brand
ORDER BY review_count DESC;

-- Conversion rate by Device
SELECT
device_type,
AVG(is_converted) * 100 AS conversion_rate
FROM sessions
GROUP BY device_type
ORDER BY conversion_rate DESC;

-- Conversion rate by Referrer Source
SELECT
referrer_source,
AVG(is_converted) * 100 AS conversion_rate
FROM sessions
GROUP BY referrer_source
ORDER BY conversion_rate DESC;

-- Most active Users
SELECT
u.user_id,
u.country,
COUNT(*) AS purchases_count
FROM purchases p
JOIN users u
	ON p.user_id = u.user_id
GROUP BY u.user_id, u.country
ORDER BY purchases_count DESC
LIMIT 10;

-- Top 10 clients by earnings
SELECT
u.user_id,
u.country,
SUM(p.total_amount) AS total_spent
FROM purchases p
JOIN users u
	ON p.user_id = u.user_id
GROUP BY u.user_id, u.country
ORDER BY total_spent DESC
LIMIT 10;
