import streamlit as st
import plotly.express as px

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
    layout="wide"
)

# -------------------------------------------------
# GLOBAL DARK THEME (ENTERPRISE)
# -------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .kpi-card {
        background-color: #161b22;
        padding: 1.5rem;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 6px 25px rgba(0,0,0,0.4);
    }
    .kpi-title {
        color: #8b949e;
        font-size: 14px;
    }
    .kpi-value {
        color: #f0f6fc;
        font-size: 30px;
        font-weight: bold;
    }
    .insight-box {
        background-color: #161b22;
        padding: 1rem;
        border-left: 4px solid #2f81f7;
        border-radius: 8px;
        color: #c9d1d9;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
# FETCH DATA
# -------------------------------------------------
total_revenue = get_total_revenue()
customer_kpis = get_customer_kpis()
region_df = revenue_by_region()
monthly_df = monthly_revenue()
ml_prediction = predict_next_month_revenue()

monthly_df["month"] = monthly_df["month"].dt.strftime("%Y-%m")

# -------------------------------------------------
# DASHBOARD OVERVIEW
# -------------------------------------------------
if page == "Dashboard Overview":

    st.title("📈 AI-Powered Enterprise Analytics Dashboard")
    st.markdown(
        "Executive-level insights powered by **SQL, Data Science, Machine Learning & AI**"
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

    fig_region = px.bar(
        region_df,
        x="region",
        y="revenue",
        color="region",
        text_auto=".2s",
        template="plotly_dark"
    )

    fig_region.update_layout(
        xaxis_title="Region",
        yaxis_title="Revenue"
    )

    st.plotly_chart(fig_region, use_container_width=True)

# -------------------------------------------------
# REVENUE TRENDS
# -------------------------------------------------
elif page == "Revenue Trends":

    st.title("📊 Monthly Revenue Growth")

    fig_trend = px.line(
        monthly_df,
        x="month",
        y="monthly_revenue",
        markers=True,
        template="plotly_dark"
    )

    fig_trend.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

# -------------------------------------------------
# AI DECISION INSIGHTS
# -------------------------------------------------
elif page == "AI Decision Insights":

    st.title("🧠 AI-Powered Decision Intelligence")

    for insight in generate_ai_insights():
        st.markdown(
            f"""
            <div class="insight-box">
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
