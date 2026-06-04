import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(base_dir, 'data', 'hr_cleaned.csv'))
output_dir = os.path.join(base_dir, 'output')

# ============================================
# BUILD RISK SCORE
# Each employee gets scored on 3 risk factors
# Score 0 = no risk factors
# Score 3 = all 3 risk factors present
# ============================================

# Risk Factor 1 - Overtime
df['risk_overtime'] = (df['OverTime'] == 'Yes').astype(int)

# Risk Factor 2 - Low Salary
# Below median income = high risk
median_income = df['MonthlyIncome'].median()
df['risk_low_salary'] = (df['MonthlyIncome'] < median_income).astype(int)

# Risk Factor 3 - Frequent Travel
df['risk_travel'] = (df['BusinessTravel'] == 'Travel_Frequently').astype(int)

# Combined Risk Score
df['risk_score'] = df['risk_overtime'] + df['risk_low_salary'] + df['risk_travel']

print("RISK SCORE DISTRIBUTION:")
print(df['risk_score'].value_counts().sort_index())

print("\nATTRITION RATE BY RISK SCORE:")
risk_analysis = df.groupby('risk_score')['Attrition_Flag'].agg(
    Total='count',
    Left='sum',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()
print(risk_analysis)

print("\nHIGHEST RISK COHORT - Sales Reps with all 3 risk factors:")
high_risk = df[
    (df['JobRole'] == 'Sales Representative') &
    (df['risk_score'] == 3)
]
print(f"Total Sales Reps with all 3 risk factors: {len(high_risk)}")
if len(high_risk) > 0:
    print(f"Attrition rate: {high_risk['Attrition_Flag'].mean()*100:.1f}%")

print("\nATTRITION BY RISK SCORE AND DEPARTMENT:")
dept_risk = df.groupby(['Department', 'risk_score'])['Attrition_Flag'].agg(
    Total='count',
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()
print(dept_risk)
