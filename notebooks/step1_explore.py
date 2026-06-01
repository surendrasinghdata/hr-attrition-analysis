import pandas as pd

# Load the dataset
df = pd.read_csv('../data/hr_attrition.csv')

# STEP 1 — How big is this dataset?
print("=" * 50)
print("SHAPE — rows and columns:")
print(df.shape)

# STEP 2 — What columns exist?
print("=" * 50)
print("COLUMN NAMES:")
for col in df.columns:
    print(col)

# STEP 3 — First 5 rows
print("=" * 50)
print("FIRST 5 ROWS:")
print(df.head())

# STEP 4 — Data types
print("=" * 50)
print("DATA TYPES:")
print(df.dtypes)

# STEP 5 — Missing values
print("=" * 50)
print("MISSING VALUES:")
print(df.isnull().sum())

# STEP 6 — How many employees left vs stayed?
# This is our TARGET variable — what we are analyzing
print("=" * 50)
print("ATTRITION — How many left vs stayed:")
print(df['Attrition'].value_counts())
print("\nAs percentage:")
print(df['Attrition'].value_counts(normalize=True) * 100)