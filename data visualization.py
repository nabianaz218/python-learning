# =====================================================================
# THE ULTIMATE DATA VISUALIZATION MASTER SCRIPT (SEABORN & MATPLOTLIB)
# =====================================================================
# This single script contains the blueprints, data-cleaning formulas, 
# and structural code for all primary chart types used in data science.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean, professional visual theme for all plots
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------------------
# 🛠️ STEP 1: GENERATE MOCK DATA (For Demonstration Purposes)
# ---------------------------------------------------------------------
# Creating a dummy dataframe to simulate real-world data traps 
# (like numbers saved as strings with unit text tags)
np.random.seed(42)
data_size = 400

mock_data = {
    'Company': np.random.choice(['Apple', 'HP', 'Dell', 'Lenovo', 'Asus'], data_size),
    'TypeName': np.random.choice(['Notebook', 'Ultrabook', 'Gaming', 'Workstation'], data_size),
    'OpSys': np.random.choice(['Windows 10', 'macOS', 'Linux', 'No OS'], data_size),
    'Weight_Raw': [f"{round(np.random.uniform(1.0, 4.5), 2)}kg" for _ in range(data_size)],
    'Price_Raw': [f"€{int(np.random.uniform(300, 3000))}" for _ in range(data_size)],
    'Satisfaction_Score': np.random.randint(1, 6, size=data_size),
    'Units_Sold': np.random.randint(5, 50, size=data_size)
}
df = pd.DataFrame(mock_data)

print("--- RAW DATA PREVIEW (With Text Traps) ---")
print(df.head(3))
print("-" * 50)


# ---------------------------------------------------------------------
# 🧹 STEP 2: DATA CLEANING & PREPROCESSING FORMULAS
# ---------------------------------------------------------------------
# Formula 1: Strip text suffixes (e.g., '1.37kg' -> 1.37 float)
df['Weight_num'] = df['Weight_Raw'].str.replace('kg', '', case=False).astype(float)

# Formula 2: Strip currency symbols and force text to numeric scales safely
df['Price_num'] = df['Price_Raw'].str.replace('€', '').astype(int)

print("\n--- CLEANED DATA PREVIEW (Ready for Plotting) ---")
print(df[['Weight_num', 'Price_num']].head(3))
print("-" * 50)


# =====================================================================
# 📊 STEP 3: THE PLOTTING DIRECTORY (ALL CHART TYPES)
# =====================================================================

# ---------------------------------------------------------------------
# CHART 1: Countplot (Categorical Headcounts Side-by-Side)
# Best Used For: Counting occurrences of categorical text groups.
# ---------------------------------------------------------------------
plt.figure(figsize=(12, 5))

sns.countplot(data=df, x='Company', hue='TypeName', palette='Set2')

plt.title("Chart 1: Distribution of Laptop Types Across Brands (Countplot)", fontsize=12, fontweight='bold')
plt.xlabel("Manufacturer (Company)")
plt.ylabel("Total Count Stocked")
plt.xticks(rotation=45) # Rotates x-axis labels to prevent text overlap
plt.legend(title="Laptop Type", bbox_to_anchor=(1.02, 1), loc='upper left') # Moves legend out of grid
plt.tight_layout() # Automatically cleans padding margins
plt.show()


# ---------------------------------------------------------------------
# CHART 2: Barplot (Comparing Averages / Means)
# Best Used For: Calculating and comparing the statistical mean of a number across groups.
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 5))

# Note: Seaborn automatically draws black confidence interval bars at the top
sns.barplot(data=df, x='TypeName', y='Price_num', palette='muted')

plt.title("Chart 2: Average Market Price by Laptop Category (Barplot)", fontsize=12, fontweight='bold')
plt.xlabel("Laptop Category (TypeName)")
plt.ylabel("Average Price (Euros)")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------
# CHART 3: Stacked Histogram (Vertical Layering / Market Share)
# Best Used For: Seeing absolute volumes and segment layers simultaneously.
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 5))

# multiple='stack' creates layers vertically, shrink adjusts space between bars
sns.histplot(data=df, x='TypeName', hue='OpSys', multiple='stack', shrink=0.8, palette='tab10')

plt.title("Chart 3: Operating System Layers within Product Categories (Stacked Bar)", fontsize=12, fontweight='bold')
plt.xlabel("Laptop Category")
plt.ylabel("Total Count")
plt.legend(title="Operating System", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------
# CHART 4: Standard Scatter Plot (Direct Continuous Value Mapping)
# Best Used For: Exploring the pure distribution and layout of numeric coordinate pairs.
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x='Weight_num', y='Price_num', hue='TypeName', palette='Dark2', alpha=0.7)

plt.title("Chart 4: Mapping Laptop Price vs. Weight (Standard Scatter Plot)", fontsize=12, fontweight='bold')
plt.xlabel("Weight (kg)")
plt.ylabel("Price (Euros)")
plt.legend(title="Laptop Type", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------
# CHART 5: Scatter Plot with Regression Trendlines (Mathematical Slopes)
# Best Used For: Finding trend directions (positive/negative correlation) between numbers.
# ---------------------------------------------------------------------
# Note: sns.lmplot handles its own canvas sizing via 'height' and 'aspect' parameters
sns.lmplot(data=df, x='Weight_num', y='Price_num', hue='TypeName', palette='Set1', height=6, aspect=1.5)

plt.title("Chart 5: Trend Analysis Between Laptop Weight and Market Price (Regression)", fontsize=12, fontweight='bold')
plt.xlabel("Weight (kg)")
plt.ylabel("Price (Euros)")
plt.grid(linestyle=':', alpha=0.5) # Adds a clean, dotted background grid line
plt.show()


# ---------------------------------------------------------------------
# CHART 6: Boxplot (Distribution Spread, Medians & Outliers)
# Best Used For: Finding data range spreads, the median point, and extreme anomalies.
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x='Company', y='Price_num', palette='pastel')

plt.title("Chart 6: Price Spread Distribution and Outlier Audit per Brand (Boxplot)", fontsize=12, fontweight='bold')
plt.xlabel("Company Brand")
plt.ylabel("Price Spectrum (Euros)")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------
# CHART 7: Pie Chart (Parts-of-a-Whole Market Percentages)
# Best Used For: Displaying static relative shares. (Requires native Matplotlib)
# ---------------------------------------------------------------------
plt.figure(figsize=(6, 6))

# Step A: Use Pandas value_counts to summarize your text column rows
brand_counts = df['Company'].value_counts()

# Step B: Pass summarized series directly into matplotlib's pie function
plt.pie(brand_counts, labels=brand_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))

plt.title("Chart 7: Total Production Share Breakdown (Pie Chart)", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------
# CHART 8: Line Plot (Continuous Numerical Trends / Timelines)
# Best Used For: Tracking how values rise or fall continuously over a sorted scale.
# ---------------------------------------------------------------------
plt.figure(figsize=(10, 5))

# Sorting by weight scale to showcase a continuous progression line
df_sorted = df.sort_values(by='Weight_num')
sns.lineplot(data=df_sorted, x='Weight_num', y='Price_num', errorbar=None, color='teal', linewidth=2)

plt.title("Chart 8: Price Trend Fluctuation Over Increasing Weight Scales (Line Plot)", fontsize=12, fontweight='bold')
plt.xlabel("Sorted Weight (kg)")
plt.ylabel("Price (Euros)")
plt.tight_layout()
plt.show()

# =====================================================================
# END OF CODE FILE - Happy Revising!
# =====================================================================