import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Raw Excel Data
df = pd.read_excel(r"C:\Users\Lenov\Downloads\Data_Analyst_Practice_Dataset.xlsx", sheet_name="Sales_Data")

# ==========================================
# STEP 1: MISSING VALUES & DUPLICATE REMOVAL
# ==========================================
print("Initial Duplicates:", df.duplicated().sum())
print("Initial Missing Values:\n", df.isnull().sum())

# Remove duplicate row (ORD-1005)
df = df.drop_duplicates()

# Fill missing values
df["Discount"] = df["Discount"].fillna(0)
df["Product_Name"] = df["Product_Name"].fillna("Unknown Product")

# ==========================================
# STEP 2: DATA VALIDATION
# ==========================================
# Standardize text casing ('north' -> 'North')
df["Region"] = df["Region"].str.strip().str.title()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Validate business rules (no negative prices/quantities, discounts between 0 and 1)
assert (df["Quantity"] > 0).all(), "Invalid Quantity found!"
assert (df["Unit_Price"] > 0).all(), "Invalid Unit Price found!"
assert df["Discount"].between(0, 1).all(), "Discount out of 0-1 range!"
print("\nData Validation Passed: All values meet business rules.")

# Calculate Net Revenue
df["Total_Revenue"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])

# ==========================================
# STEP 3: BASIC STATISTICS
# ==========================================
print("\n--- BASIC DESCRIPTIVE STATISTICS ---")
print(df[["Quantity", "Unit_Price", "Marketing_Spend", "Total_Revenue"]].describe())

# ==========================================
# STEP 4: OUTLIER DETECTION (IQR Method)
# ==========================================
Q1 = df["Quantity"].quantile(0.25)
Q3 = df["Quantity"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

outliers = df[df["Quantity"] > upper_bound]
print(f"\n--- OUTLIERS DETECTED (Quantity > {upper_bound}) ---")
print(outliers[["Order_ID", "Customer_Name", "Product_Name", "Quantity", "Total_Revenue"]])

# ==========================================
# STEP 5: CORRELATION ANALYSIS
# ==========================================
corr_matrix = df[["Quantity", "Unit_Price", "Discount", "Marketing_Spend", "Total_Revenue"]].corr()
print("\n--- CORRELATION WITH TOTAL REVENUE ---")
print(corr_matrix["Total_Revenue"].sort_values(ascending=False))

# ==========================================
# STEP 6: TREND ANALYSIS (Monthly Revenue)
# ==========================================
df["Order_Month"] = df["Order_Date"].dt.to_period("M")
monthly_trend = df.groupby("Order_Month")["Total_Revenue"].agg(["count", "sum", "mean"])
print("\n--- MONTHLY SALES TREND ---")
print(monthly_trend)

# Plot Trend & Outlier Boxplot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Boxplot for Outlier Detection
axes[0].boxplot(df["Quantity"], vert=False, patch_artist=True, boxprops=dict(facecolor="#4C72B0"))
axes[0].set_title("Order Quantity Outlier Detection")
axes[0].set_xlabel("Quantity")

# Monthly Trend Bar Chart
monthly_trend["sum"].plot(kind="bar", ax=axes[1], color="#55A868")
axes[1].set_title("Monthly Revenue Trend (Jan vs Feb 2026)")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Total Revenue (₹)")
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig("eda_visuals.png")
plt.show()

# Save Final Cleaned Dataset
df.to_excel("final_cleaned_dataset.xlsx", index=False)