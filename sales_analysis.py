import pandas as pd

print("Loading dataset...\n")

df = pd.read_csv('sales_data.csv')

print("Dataset Loaded Successfully!\n")


print("First 5 Rows:")
print(df.head())

print("\nDataset Shape (Rows, Columns):")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())


print("\nChecking Missing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])


# Data Analysis

# 1. Total Revenue
total_revenue = df['Total_Sales'].sum()

# 2. Average Sale
average_sale = df['Total_Sales'].mean()

# 3. Highest Sale
highest_sale = df['Total_Sales'].max()

# 4. Lowest Sale
lowest_sale = df['Total_Sales'].min()

# 5. Best Selling Product (by quantity)
best_product = df.groupby('Product')['Quantity'].sum().idxmax()

# 6. Region-wise Sales
region_sales = df.groupby('Region')['Total_Sales'].sum()

# 7. Monthly Sales
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total_Sales'].sum()


#Final Report Output

print("\n====================================")
print("        SALES ANALYSIS REPORT       ")
print("====================================\n")

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale Value: ₹{average_sale:,.2f}")
print(f"Highest Single Sale: ₹{highest_sale:,.2f}")
print(f"Lowest Single Sale: ₹{lowest_sale:,.2f}")
print(f"Best Selling Product: {best_product}")

print("\nTotal Sales by Region:")
print(region_sales)

print("\nMonthly Sales:")
print(monthly_sales)

print("\nReport Generated Successfully!")
