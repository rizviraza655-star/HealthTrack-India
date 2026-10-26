import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="HealthTrack India",
    layout="wide"
)
# Professional Dashboard Styling

st.markdown("""
<style>

/* Main page */
.stApp {
    background: linear-gradient(135deg, #f4f8fc 0%, #eaf2f8 100%);
    color: #1e293b;
}

/* Main content text */
[data-testid="stAppViewContainer"] p,
[data-testid="stAppViewContainer"] label,
[data-testid="stAppViewContainer"] span {
    color: #1e293b;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #12304a;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {
    color: #ffffff !important;
}

/* Sidebar dropdown */
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #ffffff !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #1e293b !important;
}

/* Main tabs */
button[data-baseweb="tab"] {
    color: #1e293b !important;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #1d4968 !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #dce6ef;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(18, 48, 74, 0.06);
}

[data-testid="stMetric"] label,
[data-testid="stMetric"] [data-testid="stMetricValue"],
[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color: #12304a !important;
}

/* Regular and download buttons */
.stButton > button,
.stDownloadButton > button {
    background-color: #1d4968 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px;
    padding: 10px 20px;
}

.stDownloadButton > button p,
.stDownloadButton > button span {
    color: #ffffff !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #2c668e !important;
    color: #ffffff !important;
}

/* Tables */
[data-testid="stDataFrame"] {
    background: #ffffff;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# Load dataset
df = pd.read_csv("HealthTrack_India_Analyzed.csv")

# Column names
insurance_col = (
    "Households with any usual member covered under a "
    "health insurance/financing scheme (%)"
)

anemia_col = "All women age 15-49 years who are anaemic22 (%)"

stunting_col = (
    "Children under 5 years who are stunted "
    "(height-for-age)18 (%)"
)

wasting_col = (
    "Children under 5 years who are wasted "
    "(weight-for-height)18 (%)"
)

# Header
st.title("HealthTrack India")
st.subheader(
    "Data-Driven Health Risk & Healthcare Accessibility Analysis"
)

st.caption(
    "District-level analysis using NFHS-5 health indicators"
)

# Sidebar filter
st.sidebar.markdown(
    "<h2 style='color: #ffffff !important;'>Dashboard Filters</h2>",
    unsafe_allow_html=True
)

states = ["All States/UTs"] + sorted(
    df["State/UT"].dropna().unique().tolist()
)

selected_state = st.sidebar.selectbox(
    "Select State/UT",
    states
)

if selected_state == "All States/UTs":
    filtered_df = df.copy()
else:
    filtered_df = df[df["State/UT"] == selected_state].copy()

# Navigation tabs
tab1, tab2, tab3 = st.tabs([
    "Overview",
    "District Analysis",
    "Cluster Analysis"
])

# ---------------- OVERVIEW ----------------
with tab1:

    # Project Overview
    st.header("Project Overview")

    st.write(
        "HealthTrack India analyzes district-level health indicators "
        "to understand healthcare accessibility and health-related "
        "patterns across India using NFHS-5 data."
    )

    st.divider()

    # Key Findings
    st.subheader("Key Findings")

    finding1, finding2 = st.columns(2)

    with finding1:
        st.info(
            "**Health Insurance Coverage**\n\n"
            "Barmer, Rajasthan recorded the highest district-level "
            "insurance coverage in the selected dataset at 97.79%."
        )

    with finding2:
        st.info(
            "**District Health Clusters**\n\n"
            "K-Means grouped 707 districts into three clusters "
            "based on selected health indicators."
        )

    st.divider()

    # Project Objective
    st.subheader("Project Objective")

    st.write(
        "This project analyzes district-level NFHS-5 health indicators "
        "to explore healthcare accessibility, maternal and child health, "
        "and selected health risks across India. The dashboard supports "
        "exploration and comparison of district-level patterns."
    )

    st.divider()

    # Dashboard Metrics
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Districts",
        filtered_df["District Names"].nunique()
    )

    col2.metric(
        "States / UTs",
        filtered_df["State/UT"].nunique()
    )

    col3.metric(
        "Health Clusters",
        filtered_df["Health_Cluster"].nunique()
    )

    st.divider()

    # Health Insurance Coverage
    st.subheader("Health Insurance Coverage")

    average_insurance = filtered_df[insurance_col].mean()

    st.metric(
        "Average Insurance Coverage",
        f"{average_insurance:.2f}%"
    )

    top_districts = filtered_df.nlargest(
        10, insurance_col
    )

    fig = px.bar(
        top_districts,
        x=insurance_col,
        y="District Names",
        color=insurance_col,
        orientation="h",
        title="Top 10 Districts by Health Insurance Coverage",
        color_continuous_scale="Blues",
        labels={
            insurance_col: "Coverage (%)",
            "District Names": "District"
        }
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        template="plotly_white",
        height=550,
        title_font=dict(
            color="#12304a",
            size=22
        ),
        font=dict(
            color="#1e293b"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # Project Methodology
    st.header("Project Methodology")

    st.markdown("""
    **1. Data Collection**

    NFHS-5 district-level health indicators were used for analysis.

    **2. Data Cleaning**

    Missing values, duplicate records, and data types were checked.
    The selected dataset contained no missing values or duplicate rows.

    **3. Exploratory Data Analysis (EDA)**

    District and state-level health indicators were explored using
    descriptive statistics and visualizations.

    **4. Correlation Analysis**

    Pearson correlation was used to examine linear relationships
    between selected health indicators.

    **5. Machine Learning**

    K-Means clustering was applied to group districts based on
    selected health indicators.

    **6. Dashboard Development**

    Streamlit and Plotly were used to build an interactive
    dashboard for exploring the results.
    """)

    st.divider()

    # Project Tools
    st.subheader("Technology Stack")

    st.write(
        "Python | Pandas | NumPy | Matplotlib | Seaborn | "
        "Scikit-learn | Plotly | Streamlit | Power BI"
    )

# ---------------- DISTRICT ANALYSIS ----------------

with tab2:

    st.header("District Health Analysis")

    st.subheader("District Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv_data,
    file_name="HealthTrack_India_District_Data.csv",
    mime="text/csv",
    key="download_filtered_data"
)

st.divider()

st.subheader("Health Indicator Comparison")

indicator_options = {
        "Women with Anemia (%)": anemia_col,
        "Children with Stunting (%)": stunting_col,
        "Children with Wasting (%)": wasting_col
    }

selected_indicator = st.selectbox(
        "Choose Health Indicator",
        list(indicator_options.keys())
    )

indicator_col = indicator_options[selected_indicator]

top_indicator_districts = filtered_df.nlargest(
        10, indicator_col
    )

fig = px.bar(
        top_indicator_districts,
        x=indicator_col,
        y="District Names",
        color=indicator_col,
        orientation="h",
        title=f"Top 10 Districts by {selected_indicator}",
        color_continuous_scale="Teal",
        labels={
            indicator_col: "Percentage",
            "District Names": "District"
        }
    )

fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        template="plotly_white"
    )

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Insurance Coverage vs Anemia")

fig = px.scatter(
        filtered_df,
        x=insurance_col,
        y=anemia_col,
        hover_name="District Names",
        color="State/UT",
        title="Insurance Coverage and Anemia Across Districts",
        labels={
            insurance_col: "Health Insurance Coverage (%)",
            anemia_col: "Women with Anemia (%)"
        }
    )

fig.update_layout(template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# ---------------- CLUSTER ANALYSIS ----------------


with tab3:

    st.header("Health Cluster Analysis")
    st.divider()

    # --------------------------------------------------
    # 1. CORRELATION ANALYSIS
    # --------------------------------------------------

    st.subheader("Correlation Between Health Indicators")

    correlation_data = filtered_df[
        [
            insurance_col,
            "Mothers who had at least 4 antenatal care visits  (for last birth in the 5 years before the survey) (%)",
            "Institutional births (in the 5 years before the survey) (%)",
            stunting_col,
            wasting_col,
            anemia_col,
            "Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)",
            "Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)"
        ]
    ].copy()

    # Short names for visualization
    correlation_data.columns = [
        "Insurance Coverage",
        "Antenatal Care",
        "Institutional Births",
        "Stunting",
        "Wasting",
        "Anemia",
        "High Blood Pressure",
        "High Blood Sugar"
    ]

    correlation = correlation_data.corr()

    fig_corr = px.imshow(
        correlation,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        aspect="equal",
        title="Correlation Between Health Indicators"
    )

    fig_corr.update_layout(
        template="plotly_white",
        height=750,
        font=dict(
            color="#1e293b",
            size=12
        ),
        title_font=dict(
            color="#12304a",
            size=22
        ),
        xaxis=dict(
            tickangle=-45,
            side="bottom"
        ),
        yaxis=dict(
            autorange="reversed"
        ),
        margin=dict(
            l=120,
            r=80,
            t=100,
            b=150
        )
    )

    st.plotly_chart(
        fig_corr,
        use_container_width=True,
        theme="streamlit"
    )

    st.info(
        "Correlation measures the strength and direction of a relationship "
        "between two indicators. Correlation does not establish causation."
    )

    st.divider()

    # --------------------------------------------------
    # 2. K-MEANS CLUSTER ANALYSIS
    # --------------------------------------------------

    st.subheader("K-Means Cluster Analysis")

    st.write(
        "K-Means clustering groups districts according to similarities "
        "in selected health indicators."
    )

    # Select health indicators
    cluster_features = [
        insurance_col,
        stunting_col,
        wasting_col,
        anemia_col,
        "Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)",
        "Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)"
    ]

    # Calculate average indicator values for each cluster
    cluster_summary = (
        filtered_df.groupby("Health_Cluster")[cluster_features]
        .mean()
        .round(2)
        .reset_index()
    )

    # Rename columns
    cluster_summary = cluster_summary.rename(
        columns={
            insurance_col: "Insurance Coverage (%)",
            stunting_col: "Stunting (%)",
            wasting_col: "Wasting (%)",
            anemia_col: "Anemia (%)",
            "Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)": "High Blood Pressure (%)",
            "Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)": "High Blood Sugar (%)"
        }
    )

    # --------------------------------------------------
    # 3. CLUSTER SUMMARY TABLE
    # --------------------------------------------------

    st.subheader("Average Health Indicators by Cluster")

    st.dataframe(
        cluster_summary,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # 4. CLUSTER COMPARISON CHART
    # --------------------------------------------------

    cluster_chart_data = cluster_summary.melt(
        id_vars="Health_Cluster",
        var_name="Health Indicator",
        value_name="Average Percentage"
    )

    fig_cluster = px.bar(
        cluster_chart_data,
        x="Health_Cluster",
        y="Average Percentage",
        color="Health Indicator",
        barmode="group",
        title="Comparison of Health Indicators Across Clusters",
        labels={
            "Health_Cluster": "Cluster",
            "Average Percentage": "Average Percentage (%)"
        },
        color_discrete_sequence=[
            "#1d4968",
            "#4f91b8",
            "#83b9d5",
            "#a8cce0",
            "#527d9b",
            "#c3dce9"
        ]
    )

    fig_cluster.update_layout(
        template="plotly_white",
        font=dict(color="#1e293b"),
        title_font=dict(
            color="#12304a",
            size=20
        )
    )

    st.plotly_chart(
        fig_cluster,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # 5. DISTRICT CLUSTER DISTRIBUTION
    # --------------------------------------------------

    st.subheader("District Cluster Distribution")

    cluster_counts = (
        filtered_df["Health_Cluster"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    cluster_counts.columns = [
        "Health_Cluster",
        "Number of Districts"
    ]

    fig_count = px.bar(
        cluster_counts,
        x="Health_Cluster",
        y="Number of Districts",
        text="Number of Districts",
        title="Number of Districts in Each Cluster",
        labels={
            "Health_Cluster": "Cluster",
            "Number of Districts": "Number of Districts"
        },
        color="Health_Cluster",
        color_discrete_sequence=[
            "#1d4968",
            "#4f91b8",
            "#83b9d5"
        ]
    )

    fig_count.update_layout(
        template="plotly_white",
        font=dict(color="#1e293b"),
        showlegend=False
    )

    st.plotly_chart(
        fig_count,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # 6. CLUSTER INTERPRETATION
    # --------------------------------------------------

    st.subheader("Understanding the Clusters")

    st.write(
        "Each cluster represents a group of districts with similar "
        "patterns across the selected health indicators."
    )

    st.write(
        "The table and charts help compare healthcare insurance coverage "
        "and health indicators such as stunting, wasting, anemia, "
        "high blood pressure, and high blood sugar."
    )

    st.info(
        "Note: Cluster numbers are labels assigned by K-Means. "
        "They do not automatically represent low, medium, or high risk. "
        "Interpret each cluster using its actual indicator values."
    )

    st.divider()

    # --------------------------------------------------
    # 7. AUTOMATIC CLUSTER FINDINGS
    # --------------------------------------------------

    st.subheader("Key Cluster Findings")

    # Highest and lowest insurance coverage
    highest_insurance = cluster_summary.loc[
        cluster_summary["Insurance Coverage (%)"].idxmax()
    ]

    lowest_insurance = cluster_summary.loc[
        cluster_summary["Insurance Coverage (%)"].idxmin()
    ]

    # Highest anemia and stunting
    highest_anemia = cluster_summary.loc[
        cluster_summary["Anemia (%)"].idxmax()
    ]

    highest_stunting = cluster_summary.loc[
        cluster_summary["Stunting (%)"].idxmax()
    ]

    # Display findings
    st.write(
        f"**Highest Insurance Coverage:** "
        f"Cluster {int(highest_insurance['Health_Cluster'])} "
        f"has the highest average insurance coverage of "
        f"{highest_insurance['Insurance Coverage (%)']:.2f}%."
    )

    st.write(
        f"**Lowest Insurance Coverage:** "
        f"Cluster {int(lowest_insurance['Health_Cluster'])} "
        f"has the lowest average insurance coverage of "
        f"{lowest_insurance['Insurance Coverage (%)']:.2f}%."
    )

    st.write(
        f"**Highest Anemia Level:** "
        f"Cluster {int(highest_anemia['Health_Cluster'])} "
        f"has the highest average anemia level of "
        f"{highest_anemia['Anemia (%)']:.2f}%."
    )

    st.write(
        f"**Highest Stunting Level:** "
        f"Cluster {int(highest_stunting['Health_Cluster'])} "
        f"has the highest average stunting level of "
        f"{highest_stunting['Stunting (%)']:.2f}%."
    )

    st.caption(
        "These findings are based on cluster averages. "
        "They describe patterns in the dataset and do not establish causation."
    )

