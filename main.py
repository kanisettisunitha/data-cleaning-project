import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Step 1: Load Data
df = pd.read_csv("data.csv")
print("Original Data:\n", df)
# Step 2: Handle Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
# Step 3: Remove Duplicates
df = df.drop_duplicates()
# Step 4: Handle Outliers (IQR Method)
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['Salary'] >= lower) & (df['Salary'] <= upper)]
print("\nCleaned Data:\n", df)
# Step 5: Visualization
# Salary Distribution
plt.figure()
sns.histplot(df['Salary'], kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()
# Department Count
plt.figure()
sns.countplot(x='Department', data=df)
plt.title("Department Count")
plt.show()
