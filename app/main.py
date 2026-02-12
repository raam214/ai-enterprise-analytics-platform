import streamlit as st
import plotly.express as px
import pandas as pd

from analytics import (
    get_total_revenue,
    get_customer_kpis,
    revenue_by_region,
    monthly_revenue
)

from ml_model import predict_next_month_revenue
from ai_insights import generate_ai_insights


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI-Powered Enterprise Analytics",
    page_icon="📊",
    layout="wide"
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

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard Overview",
        "Regional Analysis",
        "Revenue Trends",
        "AI Decision Insights"
    ]
)

st.sidebar.markdown("---")
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

# -------------------------------------------------
# DASHBOARD OVERVIEW
# -------------------------------------------------
if page == "Dashboard Overview":

    st.title("📈 AI-Powered Enterprise Analytics Dashboard")
    st.caption(
        "Executive-level insights powered by SQL, Data Science, Machine Learning & AI"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Total Revenue</div>
                <div class="kpi-value">₹ {total_revenue:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Total Customers</div>
                <div class="kpi-value">{customer_kpis['total_customers']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Active Customers</div>
                <div class="kpi-value">{customer_kpis['active_customers']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Next Month Forecast</div>
                <div class="kpi-value">₹ {ml_prediction['predicted_revenue']:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------------------------
# REGIONAL ANALYSIS
# -------------------------------------------------
elif page == "Regional Analysis":

    st.title("🌍 Revenue by Region")

    fig = px.bar(
        region_df,
        x="region",
        y="revenue",
        color="region",
        text_auto=".2s",
        template="plotly_dark"
    )

    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# REVENUE TRENDS
# -------------------------------------------------
elif page == "Revenue Trends":

    st.title("📊 Monthly Revenue Growth")

    fig = px.line(
        monthly_df,
        x="month",
        y="monthly_revenue",
        markers=True,
        template="plotly_dark"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# AI INSIGHTS
# -------------------------------------------------
elif page == "AI Decision Insights":

    st.title("🧠 AI-Powered Decision Intelligence")

    for insight in generate_ai_insights():
        st.markdown(
            f"""
            <div style="background:#161b22;
                        padding:16px;
                        border-left:5px solid #2f81f7;
                        border-radius:10px;
                        margin-bottom:12px;">
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
