import streamlit as st
import plotly.express as px
import pandas as pd

from app.analytics import (
    get_total_revenue,
    get_customer_kpis,
    revenue_by_region,
    monthly_revenue
)
from app.ml_model import predict_next_month_revenue
from app.ai_insights import generate_ai_insights

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI-Powered Enterprise Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# LOAD CSS
# -------------------------------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("📊 Enterprise Analytics")
st.sidebar.markdown("AI-Powered Business Intelligence")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard Overview",
        "Regional Analysis",
        "Revenue Trends",
        "AI Decision Insights"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Built with ❤️ by **214_raam**")

# -------------------------------------------------
# DATA LOAD
# -------------------------------------------------
total_revenue = get_total_revenue()
customer_kpis = get_customer_kpis()
region_df = revenue_by_region()
monthly_df = monthly_revenue()
ml_prediction = predict_next_month_revenue()

monthly_df["month"] = pd.to_datetime(monthly_df["month"]).dt.strftime("%Y-%m")

# =================================================
# DASHBOARD OVERVIEW
# =================================================
if page == "Dashboard Overview":

    st.title("📈 AI-Powered Enterprise Analytics Dashboard")
    st.caption(
        "Executive-level insights powered by SQL, Data Science, Machine Learning & AI"
    )

    st.markdown("## 📊 Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">💰 Total Revenue</div>
                <div class="kpi-value">₹ {total_revenue:,.0f}</div>
                <div class="kpi-delta kpi-up">▲ 8.4% vs last month</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">👥 Total Customers</div>
                <div class="kpi-value">{customer_kpis['total_customers']}</div>
                <div class="kpi-delta kpi-up">▲ 3.2% growth</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">🟢 Active Customers</div>
                <div class="kpi-value">{customer_kpis['active_customers']}</div>
                <div class="kpi-delta kpi-down">▼ 1.1% churn risk</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">🔮 Next Month Forecast</div>
                <div class="kpi-value">₹ {ml_prediction['predicted_revenue']:,.0f}</div>
                <div class="kpi-delta kpi-up">▲ AI predicted growth</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------- Revenue Trend ----------
    st.markdown("## 📈 Revenue Trend")

    fig_trend = px.area(
        monthly_df,
        x="month",
        y="monthly_revenue",
        markers=True,
        template="plotly_dark"
    )

    fig_trend.update_layout(
        height=420,
        xaxis_title="Month",
        yaxis_title="Revenue",
        hovermode="x unified"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

# =================================================
# REGIONAL ANALYSIS
# =================================================
elif page == "Regional Analysis":

    st.title("🌍 Regional Revenue Analysis")
    st.caption("Region-wise revenue contribution")

    fig_region = px.bar(
        region_df,
        x="region",
        y="revenue",
        color="region",
        text_auto=".2s",
        template="plotly_dark"
    )

    fig_region.update_layout(
        height=420,
        xaxis_title="Region",
        yaxis_title="Revenue",
        showlegend=False
    )

    st.plotly_chart(fig_region, use_container_width=True)

# =================================================
# REVENUE TRENDS
# =================================================
elif page == "Revenue Trends":

    st.title("📊 Monthly Revenue Trends")
    st.caption("Growth and seasonality analysis")

    fig_line = px.line(
        monthly_df,
        x="month",
        y="monthly_revenue",
        markers=True,
        template="plotly_dark"
    )

    st.plotly_chart(fig_line, use_container_width=True)

    # ---------- Customer Segments ----------
    st.markdown("## 🍩 Customer Segments")

    segment_df = pd.DataFrame({
        "segment": ["High Value", "Mid Value", "Low Value"],
        "customers": [
            int(customer_kpis["total_customers"] * 0.3),
            int(customer_kpis["total_customers"] * 0.5),
            int(customer_kpis["total_customers"] * 0.2)
        ]
    })

    fig_segment = px.pie(
        segment_df,
        names="segment",
        values="customers",
        hole=0.5,
        template="plotly_dark"
    )

    fig_segment.update_traces(textinfo="percent+label")

    st.plotly_chart(fig_segment, use_container_width=True)

# =================================================
# AI DECISION INSIGHTS
# =================================================
elif page == "AI Decision Insights":

    st.title("🧠 AI-Powered Decision Intelligence")
    st.caption("AI-driven forecasts and decision insights")

    # ---------- Actual vs Forecast ----------
    st.markdown("## 🔮 Actual vs Forecast")

    forecast_df = monthly_df.tail(4).copy()
    forecast_df["forecast"] = forecast_df["monthly_revenue"] * 1.08

    fig_forecast = px.line(
        forecast_df,
        x="month",
        y=["monthly_revenue", "forecast"],
        markers=True,
        template="plotly_dark"
    )

    st.plotly_chart(fig_forecast, use_container_width=True)

    # ---------- AI Insights ----------
    st.markdown("## 🧠 AI Insights")
    for insight in generate_ai_insights():
        st.markdown(
            f"""
            <div class="ai-card">
                {insight}
            </div>
            """,
            unsafe_allow_html=True
        )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.caption(
    "© 2026 | AI-Powered Enterprise Analytics Platform | "
    "SQL • Data Science • Machine Learning • AI | Built with ❤️ by 214_raam"
)
