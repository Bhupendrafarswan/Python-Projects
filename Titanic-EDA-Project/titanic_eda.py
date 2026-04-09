# Titanic EDA Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder if not exists
os.makedirs("images", exist_ok=True)

# Set style
sns.set(style="whitegrid")

# 1. Load Dataset
df = pd.read_csv("data/titanic.csv")

print("\nFirst 5 rows:")
print(df.head())

# 2. Basic Info
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 3. Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Handle Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# 5. Survival by Gender
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.savefig("images/gender_survival.png")

# 6. Survival by Class
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Class")
plt.savefig("images/class_survival.png")

# 7. Age Distribution
plt.figure()
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.savefig("images/age_distribution.png")

# 8. Age vs Survival
plt.figure()
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.savefig("images/age_survival.png")

# 9. Insights
print("\n--- Insights ---")
print("1. Females had higher survival rate than males.")
print("2. 1st class passengers survived more than 3rd class.")
print("3. Younger passengers had slightly better survival chances.")
print("4. Most passengers were between age 20–40.")
print("5. Class and gender strongly affected survival.")

print("\nEDA Completed! Check 'images' folder for visualizations.")