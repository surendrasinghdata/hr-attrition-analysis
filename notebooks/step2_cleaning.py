import pandas as pd

# Load data
df = pd.read_csv('../data/hr_attrition.csv')

print("BEFORE CLEANING:")
print(f"Shape: {df.shape}")

# ============================================
# CLEANING STEP 1 — Drop useless columns
# These 3 columns have same value for everyone
# They add zero analytical value
# ============================================

useless_columns = ['EmployeeCount', 'Over18', 'StandardHours']
df = df.drop(columns=useless_columns)

print("\nAFTER DROPPING USELESS COLUMNS:")
print(f"Shape: {df.shape}")
print(f"Dropped: {useless_columns}")

# ============================================
# CLEANING STEP 2 — Convert Attrition to number
# Currently Attrition is text: "Yes" or "No"
# We convert it to 1 and 0
# Why? Numbers are easier to calculate with
# 1 = left the company
# 0 = stayed
# ============================================

df['Attrition_Flag'] = df['Attrition'].map({'Yes': 1, 'No': 0})

print("\nATTRITION CONVERSION:")
print(df[['Attrition', 'Attrition_Flag']].head(10))

# ============================================
# CLEANING STEP 3 — Convert OverTime to number
# Same reason — Yes/No becomes 1/0
# ============================================

df['OverTime_Flag'] = df['OverTime'].map({'Yes': 1, 'No': 0})

print("\nOVERTIME CONVERSION:")
print(df[['OverTime', 'OverTime_Flag']].head(5))

# ============================================
# CLEANING STEP 4 — Check unique values
# in categorical columns
# This tells us what categories exist
# ============================================

categorical_cols = ['Department', 'JobRole',
                    'MaritalStatus', 'BusinessTravel',
                    'EducationField', 'Gender']

print("\nUNIQUE VALUES IN CATEGORICAL COLUMNS:")
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())

# Save cleaned data
df.to_csv('../data/hr_cleaned.csv', index=False)
print("\nCleaned data saved to hr_cleaned.csv")
print(f"Final shape: {df.shape}")