# HealthTrack India – Data-Driven Health Risk & Healthcare Accessibility Analysis

## Live Demo

**Explore the interactive dashboard:**  
[HealthTrack India – Live Dashboard](https://healthtrack-india.streamlit.app/)

**GitHub Repository:**  
[View Source Code](https://github.com/rizviraza655-star/HealthTrack-India)


A data analysis and visualization project that explores district-level health indicators across India using NFHS-5 data. The project uses Python, Pandas, Scikit-learn, and Streamlit to analyze healthcare accessibility, maternal health, nutrition, and health-related indicators.

## Project Overview

HealthTrack India aims to explore how healthcare access and health indicators vary across districts in India.

The project analyzes district-level data to identify patterns, compare districts, explore relationships between health indicators, and group districts using machine learning.

An interactive Streamlit dashboard allows users to explore the data and understand the findings.

## Objectives

- Analyze healthcare accessibility across Indian districts.
- Explore maternal healthcare indicators.
- Study nutrition-related indicators such as stunting, wasting, and anemia.
- Examine correlations between health indicators.
- Apply K-Means clustering to identify district-level patterns.
- Build an interactive dashboard for data exploration.

## Dataset

The project uses district-level indicators from the National Family Health Survey (NFHS-5).

The analyzed dataset contains **707 districts and 11 columns**, including district and state information along with health indicators.

### Key Indicators

- Health insurance coverage
- Antenatal care (ANC) visits
- Institutional births
- Skilled birth attendance
- Child stunting
- Child wasting
- Anemia
- Elevated blood pressure
- High blood sugar

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and application development |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib / Seaborn | Data visualization |
| Scikit-learn | StandardScaler and K-Means clustering |
| Streamlit | Interactive dashboard |
| Jupyter Notebook | Data exploration and analysis |
| Git & GitHub | Version control and project hosting |

## Project Features

### 1. Overview Dashboard
Provides a summary of the dataset and key health indicators.

### 2. District Analysis
Allows users to explore and compare health indicators across districts.

### 3. Cluster Analysis
Uses K-Means clustering to group districts based on selected health indicators.

### 4. Correlation Analysis
Explores relationships between healthcare accessibility and health indicators.

## Key Findings

- Health insurance coverage showed a positive correlation with ANC visits (approximately 0.245).
- A positive correlation was also observed between insurance coverage and skilled birth attendance (approximately 0.195).
- Insurance coverage showed a positive correlation with institutional births (approximately 0.181).
- K-Means clustering identified three groups of districts with different indicator patterns.
- District-level health indicators vary considerably across the dataset.

**Note:** Correlation does not imply causation. The cluster labels represent algorithm-generated groups and should not be interpreted as official health-risk categories.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/rizviraza655-star/HealthTrack-India.git
```

### 2. Navigate to the Project Folder

```bash
cd HealthTrack-India
```

### 3. Install Required Libraries

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn
```

### 4. Run the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open in your default web browser.

## Project Structure

```text
HealthTrack-India/
│
├── app.py
├── Main.py
├── HealthTrack_India_Analyzed.csv
├── NFHS_5_India_Districts_Factsheet_Data.xls
├── .gitignore
└── README.md
```

## Limitations

- The analysis is based on district-level data and does not represent individual-level health outcomes.
- Correlation analysis cannot establish causal relationships.
- K-Means clustering depends on the selected features and preprocessing.
- The findings should be interpreted as exploratory analysis, not medical advice.

## Future Improvements

- Add more health and demographic indicators.
- Improve dashboard filters and visualizations.
- Add district-level maps.
- Deploy the dashboard online.
- Explore additional clustering and statistical methods.

## Academic Project

**University:** Shri Ramswaroop Memorial University  
**Department:** Data Science and Artificial Intelligence  
**Semester:** 5th Semester  
**Project Team:** Data Medics  
**Submitted By:** Syed Mohd Raza Rizvi  
**Roll Number:** 202410101150086  
**Project Guide:** [Add Guide Name]

## Acknowledgement

This project uses district-level health data from NFHS-5. The project was developed for academic learning and exploratory data analysis.

## License

This project is intended for educational and academic purposes.
