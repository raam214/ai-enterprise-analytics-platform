import pandas as pd
from db import get_engine


def get_total_revenue():
    query = "SELECT COALESCE(SUM(amount),0) AS total_revenue FROM transactions"
    df = pd.read_sql(query, get_engine())
    return float(df.iloc[0]["total_revenue"])


def get_customer_kpis():
    query = """
    SELECT 
        COUNT(*) AS total_customers,
        COUNT(*) FILTER (WHERE is_active = true) AS active_customers
    FROM customers
    """
    df = pd.read_sql(query, get_engine())
    return {
        "total_customers": int(df.iloc[0]["total_customers"]),
        "active_customers": int(df.iloc[0]["active_customers"])
    }


def revenue_by_region():
    query = """
    SELECT c.region, SUM(t.amount) AS revenue
    FROM transactions t
    JOIN customers c ON t.customer_id = c.customer_id
    GROUP BY c.region
    ORDER BY revenue DESC
    """
    return pd.read_sql(query, get_engine())


def monthly_revenue():
    query = """
    SELECT DATE_TRUNC('month', transaction_date) AS month,
           SUM(amount) AS monthly_revenue
    FROM transactions
    GROUP BY month
    ORDER BY month
    """
    return pd.read_sql(query, get_engine())
