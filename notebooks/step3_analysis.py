import pandas as pd

# Load cleaned data
df = pd.read_csv('../data/hr_cleaned.csv')

# ============================================
# ANALYSIS 1 — Attrition by Department
# Which department loses most employees?
# ============================================

print("=" * 50)
print("ATTRITION BY DEPARTMENT:")
dept_attrition = df.groupby('Department')['Attrition_Flag'].agg(
    Total='count',
    Left='sum',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()
print(dept_attrition)

# ============================================
# ANALYSIS 2 — Attrition by Job Role
# Which roles have highest turnover?
# ============================================

print("\n" + "=" * 50)
print("ATTRITION BY JOB ROLE:")
role_attrition = df.groupby('JobRole')['Attrition_Flag'].agg(
    Total='count',
    Left='sum',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index().sort_values('Attrition_Rate', ascending=False)
print(role_attrition)

# ============================================
# ANALYSIS 3 — Income comparison
# Do employees who left earn less?
# ============================================

print("\n" + "=" * 50)
print("MONTHLY INCOME — Left vs Stayed:")
income_comparison = df.groupby('Attrition')['MonthlyIncome'].agg(
    Average='mean',
    Median='median',
    Min='min',
    Max='max'
).round(2)
print(income_comparison)

# ============================================
# ANALYSIS 4 — Overtime impact
# Does working overtime cause people to leave?
# ============================================

print("\n" + "=" * 50)
print("ATTRITION BY OVERTIME:")
overtime_attrition = df.groupby('OverTime')['Attrition_Flag'].agg(
    Total='count',
    Left='sum',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()
print(overtime_attrition)

# ============================================
# ANALYSIS 5 — Age analysis
# Are younger employees leaving more?
# ============================================

print("\n" + "=" * 50)
print("AGE COMPARISON — Left vs Stayed:")
age_comparison = df.groupby('Attrition')['Age'].agg(
    Average='mean',
    Median='median',
    Min='min',
    Max='max'
).round(2)
print(age_comparison)

# ============================================
# ANALYSIS 6 — Job Satisfaction
# Do unhappy employees leave more?
# ============================================

print("\n" + "=" * 50)
print("ATTRITION BY JOB SATISFACTION:")
print("(1=Low, 2=Medium, 3=High, 4=Very High)")
satisfaction = df.groupby('JobSatisfaction')['Attrition_Flag'].agg(
    Total='count',
    Left='sum',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()
print(satisfaction)

# ============================================
# ANALYSIS 7 — Years at company
# Do new employees leave faster?
# ============================================

print("\n" + "=" * 50)
print("YEARS AT COMPANY — Left vs Stayed:")
years_comparison = df.groupby('Attrition')['YearsAtCompany'].agg(
    Average='mean',
    Median='median'
).round(2)
print(years_comparison)

# ============================================
# ANALYSIS 8 — Business Travel
# Does frequent travel cause attrition?
# ============================================

print("\n" + "=" * 50)
print("ATTRITION BY BUSINESS TRAVEL:")
travel_attrition = df.groupby('BusinessTravel')['Attrition_Flag'].agg(
    Total='count',
    Left='sum',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index().sort_values('Attrition_Rate', ascending=False)
print(travel_attrition)