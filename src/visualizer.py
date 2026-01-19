import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output folder exists
def ensure_output_folder():
    os.makedirs("../outputs/plots/", exist_ok=True)

# 1. Histogram for numerical features
def plot_hist(df, column):
    ensure_output_folder()
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True, color='darkblue')
    plt.title(f"Distribution of {column}", fontsize=14)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.savefig(f"../outputs/plots/{column}_hist.png")
    plt.show()

# 2. Countplot for categorical features
def plot_count(df, column):
    ensure_output_folder()
    plt.figure(figsize=(12, 5))
    sns.countplot(data=df, x=column, palette="viridis")
    plt.xticks(rotation=45)
    plt.title(f"Count Plot for {column}", fontsize=14)
    plt.savefig(f"../outputs/plots/{column}_count.png")
    plt.show()

# 3. Boxplot for outlier detection
def plot_box(df, column):
    ensure_output_folder()
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x=column, color='orange')
    plt.title(f"Box Plot for {column}", fontsize=14)
    plt.savefig(f"../outputs/plots/{column}_box.png")
    plt.show()

# 4. Correlation heatmap
def plot_correlation(df, title="Correlation Heatmap"):
    ensure_output_folder()
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(title, fontsize=16)
    plt.savefig("../outputs/plots/correlation_heatmap.png")
    plt.show()
