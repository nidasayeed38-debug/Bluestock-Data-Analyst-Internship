import pandas as pd
import numpy as np
from scipy import stats

# Load your cleaned dataset (update path if needed)
df = pd.read_excel(r"C:\Users\lenov\OneDrive\Desktop\Core Data Analytics Foundation\Task_1 Fundamental Technical skills.xlsx")

# ==========================================
# 1. MEAN, MEDIAN, MODE (Central Tendency)
# ==========================================
mean_rev = df["Calculate Total Revenue"].mean()
median_rev = df["Calculate Total Revenue"].median()
mode_cat = df["Product_Category"].mode()[0]
mode_qty = df["Quantity"].mode()[0]

print("--- 1. CENTRAL TENDENCY ---")
print(f"Mean Order Revenue:   ₹{mean_rev:,.2f}")
print(f"Median Order Revenue: ₹{median_rev:,.2f}")
print(f"Mode (Category):      {mode_cat}")
print(f"Mode (Quantity):      {mode_qty} units")

# ==========================================
# 2. STANDARD DEVIATION (Spread / Volatility)
# ==========================================
std_rev = df["Calculate Total Revenue"].std()
std_qty = df["Quantity"].std()

print("\n--- 2. STANDARD DEVIATION ---")
print(f"Revenue Std Dev:      ₹{std_rev:,.2f}")
print(f"Quantity Std Dev:     {std_qty:.2f} units")

# ==========================================
# 3. CORRELATION (Relationship Strength)
# ==========================================
corr_spend_rev = df["Marketing_Spend"].corr(df["Calculate Total Revenue"])
corr_qty_rev = df["Quantity"].corr(df["Calculate Total Revenue"])

print("\n--- 3. CORRELATION (Pearson r) ---")
print(f"Marketing Spend vs. Revenue: {corr_spend_rev:.4f}")
print(f"Quantity vs. Revenue:        {corr_qty_rev:.4f}")

# ==========================================
# 4. PROBABILITY BASICS
# ==========================================
total_orders = len(df)
high_value_orders = len(df[df["Calculate Total Revenue"] > 5000])
prob_high_value = high_value_orders / total_orders

# Conditional Probability: P(Revenue > 5000 | Category = Electronics)
electronics_df = df[df["Product_Category"] == "Electronics"]
prob_high_given_elec = len(electronics_df[electronics_df["Calculate Total Revenue"] > 5000]) / len(electronics_df)

print("\n--- 4. PROBABILITY BASICS ---")
print(f"P(Order > ₹5,000):               {prob_high_value:.2%} ({high_value_orders}/{total_orders} orders)")
print(f"P(Order > ₹5,000 | Electronics): {prob_high_given_elec:.2%}")

# ==========================================
# 5. LINEAR REGRESSION (Introduction)
# ==========================================
# Predict Total_Revenue (Y) based on Marketing_Spend (X)
slope, intercept, r_value, p_value, std_err = stats.linregress(
    df["Marketing_Spend"], df["Calculate Total Revenue"]
)

# Example Prediction: Expected revenue if we spend ₹1,000 on marketing
predicted_rev = intercept + slope * 1000

print("\n--- 5. SIMPLE LINEAR REGRESSION ---")
print(f"Equation: Calculate Total Revenue = {intercept:.2f} + ({slope:.2f} × Marketing_Spend)")
print(f"R-squared: {r_value*2:.4f} (Explains {r_value*2:.1%} of revenue variance)")
print(f"P-value:   {p_value:.6f} (Statistically significant if < 0.05)")
print(f"Predicted Revenue for ₹1,000 Marketing Spend: ₹{predicted_rev:,.2f}")