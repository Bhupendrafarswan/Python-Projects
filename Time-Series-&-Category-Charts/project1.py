import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Step 1: Create sample dataset
np.random.seed(0)

dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
categories = ['Electronics', 'Clothing', 'Furniture']

data = pd.DataFrame({
    'Date': np.random.choice(dates, 200),
    'Category': np.random.choice(categories, 200),
    'Sales': np.random.randint(100, 1000, 200)
})

# Step 2: Save dataset
data.to_csv('sales_data.csv', index=False)

# Step 3: Load dataset
data = pd.read_csv('sales_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

# Step 4: Line Chart (Daily Sales)
daily_sales = data.groupby('Date')['Sales'].sum()

plt.figure()
daily_sales.plot()
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("line_chart.png")
plt.show()

# Step 5: Monthly Sales
data.set_index('Date', inplace=True)

monthly_sales = data['Sales'].resample('ME').sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_chart.png")
plt.show()

# Step 6: Bar Chart
category_sales = data.groupby('Category')['Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")
plt.show()

# Step 7: Pie Chart
plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Share")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.show()

print("✅ Project completed! Charts saved.")