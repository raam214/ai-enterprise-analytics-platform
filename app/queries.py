TOTAL_REVENUE = """
SELECT COALESCE(SUM(amount), 0) AS total_revenue FROM transactions;
"""

CUSTOMER_KPIS = """
SELECT
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE is_active = TRUE) AS active_customers
FROM customers;
"""

REVENUE_BY_REGION = """
SELECT c.region, SUM(t.amount) AS revenue
FROM transactions t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY c.region
ORDER BY revenue DESC;
"""

MONTHLY_REVENUE = """
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(amount) AS monthly_revenue
FROM transactions
GROUP BY month
ORDER BY month;
"""
