import pandas as pd
from db import get_engine
from queries import (
    TOTAL_REVENUE_QUERY,
    CUSTOMER_KPI_QUERY,
    REVENUE_BY_REGION_QUERY,
    MONTHLY_REVENUE_QUERY
)


engine = get_engine()


def get_total_revenue():
    df = pd.read_sql(TOTAL_REVENUE, engine)
    return float(df.iloc[0]["total_revenue"])


def get_customer_kpis():
    df = pd.read_sql(CUSTOMER_KPIS, engine)
    return {
        "total_customers": int(df.iloc[0]["total_customers"]),
        "active_customers": int(df.iloc[0]["active_customers"]),
    }


def revenue_by_region():
    return pd.read_sql(REVENUE_BY_REGION, engine)


def monthly_revenue():
    return pd.read_sql(MONTHLY_REVENUE, engine)
