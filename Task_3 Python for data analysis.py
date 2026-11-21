# ==========================================
# 1. LIBRARIES (Pandas, NumPy, Matplotlib)
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 2. FILE HANDLING & VARIABLES (Load Excel)
# ==========================================
input_file = r"C:\Users\lenov\Downloads\Data_Analyst_Practice_Dataset.xlsx"
output_excel = "cleaned_sales_data.xlsx"
output_csv = "cleaned_sales_data.csv"

# Load the 'Sales_Data' tab directly from the Excel workbook
df = pd.read_excel(input_file, sheet_name="Sales_Data")
print("Raw Excel Dataset Loaded. Total rows:", len(df))

# ==========================================
# 3. DATA CLEANING (Pandas)
# ==========================================
# Remove duplicate rows (fixes duplicate ORD-1005)
df = df.drop_duplicates()

# Standardize text casing (fixes lowercase 'north' -> 'North')
df["Region"] = df["Region"].str.strip().str.title()

# Fill missing values (fixes blank Discount and Product_Name)
df["Discount"] = df["Discount"].fillna(0)
df["Product_Name"] = df["Product_Name"].fillna("Unknown Product")

# Convert Order_Date to datetime format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# ==========================================
# 4. FUNCTIONS & NUMPY (Calculate KPIs)
# ==========================================
# Reusable function to compute net revenue after discount
def compute_net_revenue(quantity, unit_price, discount):
    return quantity * unit_price * (1 - discount)

# Apply function to create a new column
df["Total_Revenue"] = compute_net_revenue(
    df["Quantity"], df["Unit_Price"], df["Discount"]
)

# Use NumPy to calculate statistical KPIs
total_revenue = np.sum(df["Total_Revenue"])
avg_order_value = np.mean(df["Total_Revenue"])
median_order_value = np.median(df["Total_Revenue"])
total_units = np.sum(df["Quantity"])
total_orders = len(df)

# ==========================================
# 5. LISTS, DICTIONARIES & LOOPS
# ==========================================
# Store KPI names in a List and values in a Dictionary
kpi_labels = [
    "Total Revenue",
    "Total Orders",
    "Total Units Sold",
    "Average Order Value",
    "Median Order Value"
]

kpi_summary = {
    "Total Revenue": f"₹{total_revenue:,.2f}",
    "Total Orders": total_orders,
    "Total Units Sold": total_units,
    "Average Order Value": f"₹{avg_order_value:,.2f}",
    "Median Order Value": f"₹{median_order_value:,.2f}"
}

# Loop through the list to print each KPI from the dictionary
print("\n--- BUSINESS KPI SUMMARY ---")
for label in kpi_labels:
    print(f"{label}: {kpi_summary[label]}")

# ==========================================
# 6. FILE HANDLING (Export Cleaned Files)
# ==========================================
# Export as both Excel and CSV so you have both formats ready
df.to_excel(output_excel, sheet_name="Cleaned_Sales", index=False)
df.to_csv(output_csv, index=False)
print(f"\nCleaned data saved to '{output_excel}' and '{output_csv}'.")

# ==========================================
# 7. VISUALIZATIONS (Matplotlib)
# ==========================================
# Visualization 1: Bar Chart of Revenue by Region
region_rev = df.groupby("Region")["Total_Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 4))
plt.bar(region_rev.index, region_rev.values, color="#2b5c8f")
plt.title("Total Revenue by Region", fontsize=13, fontweight="bold")
plt.xlabel("Region")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()

# Visualization 2: Pie Chart of Revenue Share by Category
cat_rev = df.groupby("Product_Category")["Total_Revenue"].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    cat_rev.values,
    labels=cat_rev.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#2b5c8f", "#4caf50", "#ff9800"]
)
plt.title("Revenue Share by Product Category", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()
