import pandas as pd
import numpy as np

df = pd.read_excel("NFHS_5_India_Districts_Factsheet_Data.xls")

#Understanding the Dataset

#Displaying the first few rows of the dataset
print(df.head())

# Displaying the shape and columns of the dataset
print(df.shape)

#Displaying the column names of the dataset
print(df.columns)

#Dataset Information
print("\nDataset Information:")
df.info()

#Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

#Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

#Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

#Data Cleaning
# Display all column names
print("Dataset Columns:")
for column in df.columns:
    print(column)

# Select Important Features

selected_columns = [
    "District Names",
    "State/UT",
    "Households with any usual member covered under a health insurance/financing scheme (%)",
    "Mothers who had at least 4 antenatal care visits  (for last birth in the 5 years before the survey) (%)",
    "Institutional births (in the 5 years before the survey) (%)",
    "Births attended by skilled health personnel (in the 5 years before the survey)10 (%)",
    "Children under 5 years who are stunted (height-for-age)18 (%)",
    "Children under 5 years who are wasted (weight-for-height)18 (%)",
    "All women age 15-49 years who are anaemic22 (%)",
    "Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)",
    "Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)"
]

df_selected = df[selected_columns]

print(df_selected.head())
print(df_selected.shape)

# Step 5: Data Cleaning

# Check missing values
print("Missing Values:")
print(df_selected.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df_selected.duplicated().sum())

# Remove duplicate rows
df_selected = df_selected.drop_duplicates()

# Check dataset shape after removing duplicates
print("\nDataset Shape After Removing Duplicates:")
print(df_selected.shape)

# Check data types
print("\nData Types:")
print(df_selected.dtypes)

print("\nDataset Summary:")


#Top and bottom districts
#identify districts with the highest and lowest health insurance coverage.

insurance_col = "Households with any usual member covered under a health insurance/financing scheme (%)"

top_districts = df_selected.nlargest(10, insurance_col)[["District Names", "State/UT", insurance_col]]
bottom_districts = df_selected.nsmallest(10, insurance_col)[["District Names", "State/UT", insurance_col]]

print("Top 10 Districts by Health Insurance Coverage:")
print(top_districts)

print("\nBottom 10 Districts by Health Insurance Coverage:")
print(bottom_districts)

# Compare health indicators across states
state_avg = df_selected.groupby("State/UT").mean(numeric_only=True)

print("Average Health Indicators by State/UT:")
print(state_avg)

print("\nAverage Health Insurance Coverage by State/UT:")
print(state_avg[
    "Households with any usual member covered under a health insurance/financing scheme (%)"
].sort_values(ascending=False))

#Top 10 States/UTs by Average Health Insurance Coverage.

import matplotlib.pyplot as plt
import seaborn as sns

insurance_col = "Households with any usual member covered under a health insurance/financing scheme (%)"

state_avg = df_selected.groupby("State/UT").mean(numeric_only=True)

top_states = state_avg[insurance_col].sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_states.values, y=top_states.index)

plt.title("Top 10 States/UTs by Average Health Insurance Coverage")
plt.xlabel("Coverage (%)")
plt.ylabel("State/UT")

plt.show()

#Graph 2: Health Insurance Coverage vs. Anemia in Women.
insurance_col = "Households with any usual member covered under a health insurance/financing scheme (%)"
anemia_col = "All women age 15-49 years who are anaemic22 (%)"

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_selected,
    x=insurance_col,
    y=anemia_col
)

plt.title("Health Insurance Coverage vs Anemia in Women")
plt.xlabel("Health Insurance Coverage (%)")
plt.ylabel("Women with Anemia (%)")

plt.show()

#Graph 3: Correlation Heatmap of Health Indicators.
health_data = df_selected.select_dtypes(include="number")

correlation = health_data.corr()

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Health Indicators")
plt.show()

#Find the strongest relationships
#Correlation Analysis

correlation = df_selected.select_dtypes(include="number").corr()

insurance_col = "Households with any usual member covered under a health insurance/financing scheme (%)"

insurance_corr = correlation[insurance_col].drop(insurance_col)

print("Correlation with Health Insurance Coverage:")
print(insurance_corr.sort_values(ascending=False))

# Step 10: District Health Risk Clustering using K-Means

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Select health indicators for clustering
features = [
    "Households with any usual member covered under a health insurance/financing scheme (%)",
    "Children under 5 years who are stunted (height-for-age)18 (%)",
    "Children under 5 years who are wasted (weight-for-height)18 (%)",
    "All women age 15-49 years who are anaemic22 (%)",
    "Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)",
    "Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)"
]

X = df_selected[features].copy()

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df_selected["Health_Cluster"] = kmeans.fit_predict(X_scaled)

print("Districts grouped into clusters:")
print(df_selected[["District Names", "State/UT", "Health_Cluster"]].head(20))

print("\nNumber of districts in each cluster:")
print(df_selected["Health_Cluster"].value_counts().sort_index())

# Step 11: Analyze Cluster Characteristics

cluster_summary = df_selected.groupby("Health_Cluster")[features].mean()

print("Average Health Indicators for Each Cluster:")
print(cluster_summary.round(2))

print("\nNumber of Districts in Each Cluster:")
print(df_selected["Health_Cluster"].value_counts().sort_index())

#Display the complete cluster summary
pd.set_option("display.max_columns", None)

print("\nComplete Cluster Summary:")
print(cluster_summary.round(2).T)

# Step 13: Compare Health Risks Across Clusters

risk_features = [
    "Children under 5 years who are stunted (height-for-age)18 (%)",
    "Children under 5 years who are wasted (weight-for-height)18 (%)",
    "All women age 15-49 years who are anaemic22 (%)"
]

cluster_risks = df_selected.groupby("Health_Cluster")[risk_features].mean()

cluster_risks.columns = ["Stunting (%)", "Wasting (%)", "Anemia (%)"]

cluster_risks.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Comparison of Health Indicators Across District Clusters")
plt.xlabel("Health Cluster")
plt.ylabel("Average Percentage")
plt.xticks(rotation=0)
plt.legend(title="Health Indicators")
plt.show()

# Step 14: Export Final Dataset

df_selected.to_csv("HealthTrack_India_Analyzed.csv", index=False)

print("Analyzed dataset saved successfully!")