import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from db import get_engine


def predict_next_month_revenue():
    query = """
    SELECT DATE_TRUNC('month', transaction_date) AS month,
           SUM(amount) AS revenue
    FROM transactions
    GROUP BY month
    ORDER BY month
    """
    df = pd.read_sql(query, get_engine())

    df["index"] = np.arange(len(df))
    X = df[["index"]]
    y = df["revenue"]

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(df)]])[0]
    next_month = (df["month"].max() +
                  pd.DateOffset(months=1)).strftime("%B %Y")

    return {
        "next_month": next_month,
        "predicted_revenue": float(prediction)
    }
