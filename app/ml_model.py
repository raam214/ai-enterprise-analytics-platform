import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from db import get_engine


engine = get_engine()


def predict_next_month_revenue():
    df = pd.read_sql(
        """
        SELECT DATE_TRUNC('month', transaction_date) AS month,
               SUM(amount) AS revenue
        FROM transactions
        GROUP BY month
        ORDER BY month
        """,
        engine
    )

    df["index"] = np.arange(len(df))
    X = df[["index"]]
    y = df["revenue"]

    model = LinearRegression()
    model.fit(X, y)

    next_index = [[len(df)]]
    prediction = model.predict(next_index)[0]

    return {
        "next_month": df["month"].iloc[-1] + pd.DateOffset(months=1),
        "predicted_revenue": float(prediction)
    }
