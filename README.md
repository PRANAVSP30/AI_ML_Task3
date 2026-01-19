# AI & ML Internship – Task 3
## Exploratory Data Analysis (EDA)
### Dataset: Netflix Movies & TV Shows  
**Submitted by : Pranav S P**

---

#  Project Overview

This project focuses on performing **Exploratory Data Analysis (EDA)** on the Netflix dataset to understand content patterns, ratings distribution, outliers, and correlations.

A custom EDA module (`visualizer.py`) was created to keep the analysis modular, reusable, and professional.

---

#  Project Structure

```
AI_ML_Task3/
│
├── data/
│   └── netflix_titles.csv
│
├── src/
│   └── visualizer.py
│
├── notebooks/
│   └── eda.ipynb
│
├── outputs/
│   ├── plots/
│   └── screenshots/
│
├── reports/
│   └── task3_eda_report.md
│
└── README.md
```

---

# Tech Stack Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- VS Code / Jupyter Notebook  
- Git & GitHub  

---

#  Key EDA Activities Performed

## 1️. Dataset Understanding
- Checked dataset shape  
- Reviewed column types  
- Inspected missing values  
- Verified unique category values  

---

## 2️. Visual Analysis

###  Count Plots  
- Movies vs TV Shows  
- Ratings distribution  

###  Histogram  
- Distribution of engineered feature `title_length`

###  Boxplot  
- Detection of outliers in title length  

###  Correlation Heatmap  
- Relationship between `release_year` and `title_length`

###  All plots saved in:
```
outputs/plots/
```

---

#  Key Insights from EDA

##  1. Content Type
- Netflix has more **Movies** than TV Shows.  
  → Movies dominate the content library.

---

##  2. Ratings Distribution
- **TV-MA** is the most common rating.  
  → Indicates a large amount of mature content.

---

##  3. Title Length Behavior
- Most titles fall between **5–20 characters**.  
  → Titles are short, simple, and user-friendly.

---

##  4. Outlier Detection
- Some titles have unusually long names.  
  → Likely documentaries or special cases.

---

##  5. Correlation Insights
- No strong correlation between `release_year` and `title_length`.  
  → Naming style has not changed significantly over time.

---

#  Files Included

| File / Folder | Description |
|--------------|-------------|
| `notebooks/eda.ipynb` | Main EDA notebook |
| `src/visualizer.py` | Custom reusable plotting module |
| `data/netflix_titles.csv` | Raw dataset |
| `outputs/plots/` | Saved graphs |
| `reports/task3_eda_report.md` | EDA summary report |
| `README.md` | Project documentation |

---


This project demonstrates **clean analysis, modular coding, and professional documentation** expected in real-world data science.

---

# 🎉 End of README
