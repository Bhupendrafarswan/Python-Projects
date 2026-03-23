import pandas as pd
import os

# Create output folder if not exists
if not os.path.exists("output"):
    os.makedirs("output")

print("📂 Loading dataset...")

# 1. Read CSV file
df = pd.read_csv("data.csv")

# 2. Show basic info
print("\n📊 First 5 rows:")
print(df.head())

print("\n📊 Last 5 rows:")
print(df.tail())

print("\n📊 Data Types:")
print(df.dtypes)

print("\n📊 Dataset Info:")
print(df.info())

# 3. Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# 4. Column-wise statistics
print("\n💰 Salary Analysis:")
print("Mean Salary:", df["Salary"].mean())
print("Max Salary:", df["Salary"].max())
print("Min Salary:", df["Salary"].min())

# 5. Filtering data
print("\n🔍 Employees with Salary > 30000:")
high_salary = df[df["Salary"] > 30000]
print(high_salary)

# 6. Select specific columns
print("\n📌 Name & Salary:")
print(df[["Name", "Salary"]])

# 7. Group by department
print("\n🏢 Average Salary by Department:")
dept_salary = df.groupby("Department")["Salary"].mean()
print(dept_salary)

# 8. Sorting data
print("\n📈 Sorted by Salary (High to Low):")
sorted_df = df.sort_values(by="Salary", ascending=False)
print(sorted_df)

# 9. Save outputs
high_salary.to_csv("output/high_salary.csv", index=False)
dept_salary.to_csv("output/department_salary.csv")

print("\n✅ Files saved in 'output' folder!")

# 10. Extra: Count employees per department
print("\n👥 Employee Count by Department:")
print(df["Department"].value_counts())

print("\n🎉 Project Completed Successfully!")