# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("/content/Loan 2.csv")


# Print the column names
print(df.columns)

# Handle null values
null_values = df.isnull().sum()
print("Null values before handling:")
print(null_values)

# Fill null values with appropriate values
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Income (USD)'] = df['Income (USD)'].fillna(df['Income (USD)'].median())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Income Stability'] = df['Income Stability'].fillna(df['Income Stability'].mode()[0])
df['Profession'] = df['Profession'].fillna(df['Profession'].mode()[0])
df['Type of Employment'] = df['Type of Employment'].fillna(df['Type of Employment'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
df['Loan Amount Request (USD)'] = df['Loan Amount Request (USD)'].fillna(df['Loan Amount Request (USD)'].median())
df['Current Loan Expenses (USD)'] = df['Current Loan Expenses (USD)'].fillna(df['Current Loan Expenses (USD)'].median())
df['Expense Type 1'] = df['Expense Type 1'].fillna(df['Expense Type 1'].mode()[0])
df['Expense Type 2'] = df['Expense Type 2'].fillna(df['Expense Type 2'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].median())
df['Credit Score'] = df['Credit Score'].fillna(df['Credit Score'].mean())
df['No. of Defaults'] = df['No. of Defaults'].fillna(df['No. of Defaults'].median())
df['Has Active Credit Card'] = df['Has Active Credit Card'].fillna(df['Has Active Credit Card'].mode()[0])
df['Property ID'] = df['Property ID'].fillna(df['Property ID'].mode()[0])
df['Property Age'] = df['Property Age'].fillna(df['Property Age'].median())
df['Property Type'] = df['Property Type'].fillna(df['Property Type'].mode()[0])
df['Property Location'] = df['Property Location'].fillna(df['Property Location'].mode()[0])
df['Co-Applicant'] = df['Co-Applicant'].fillna(df['Co-Applicant'].mode()[0])
df['Property Price'] = df['Property Price'].fillna(df['Property Price'].median())
df['Loan Sanction Amount (USD)'] = df['Loan Sanction Amount (USD)'].fillna(df['Loan Sanction Amount (USD)'].median())