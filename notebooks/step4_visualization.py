import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(base_dir, 'data', 'hr_cleaned.csv'))
output_dir = os.path.join(base_dir, 'output')
sns.set_style("whitegrid")

# CHART 1 - Attrition by Job Role
role_attrition = df.groupby('JobRole')['Attrition_Flag'].mean().sort_values(ascending=False) * 100
fig, ax = plt.subplots(figsize=(12, 6))
colors = ['#F44336' if x > 20 else '#FF9800' if x > 10 else '#4CAF50' for x in role_attrition.values]
bars = ax.barh(role_attrition.index, role_attrition.values, color=colors)
ax.axvline(x=df['Attrition_Flag'].mean()*100, color='black', linestyle='--', label='Company Average')
ax.set_xlabel('Attrition Rate (%)')
ax.set_title('Attrition Rate by Job Role', fontweight='bold', fontsize=13)
ax.legend()
for bar, val in zip(bars, role_attrition.values):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, f'{val:.1f}%', va='center', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart1_attrition_by_role.png'), dpi=150, bbox_inches='tight')
print("Chart 1 saved")
plt.close()

# CHART 2 - Overtime vs Attrition
overtime_data = df.groupby('OverTime')['Attrition_Flag'].mean() * 100
fig, ax = plt.subplots(figsize=(8, 6))
colors2 = ['#4CAF50', '#F44336']
bars2 = ax.bar(overtime_data.index, overtime_data.values, color=colors2, width=0.4)
ax.set_ylabel('Attrition Rate (%)')
ax.set_title('Impact of Overtime on Attrition', fontweight='bold', fontsize=13)
for bar, val in zip(bars2, overtime_data.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, f'{val:.1f}%', ha='center', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart2_overtime_attrition.png'), dpi=150, bbox_inches='tight')
print("Chart 2 saved")
plt.close()

# CHART 3 - Income distribution Left vs Stayed
fig, ax = plt.subplots(figsize=(10, 6))
df[df['Attrition']=='No']['MonthlyIncome'].hist(bins=30, alpha=0.6, color='#4CAF50', label='Stayed', ax=ax)
df[df['Attrition']=='Yes']['MonthlyIncome'].hist(bins=30, alpha=0.6, color='#F44336', label='Left', ax=ax)
ax.set_xlabel('Monthly Income (USD)')
ax.set_ylabel('Number of Employees')
ax.set_title('Income Distribution - Left vs Stayed', fontweight='bold', fontsize=13)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart3_income_distribution.png'), dpi=150, bbox_inches='tight')
print("Chart 3 saved")
plt.close()

# CHART 4 - Attrition by Business Travel
travel_data = df.groupby('BusinessTravel')['Attrition_Flag'].mean().sort_values(ascending=False) * 100
fig, ax = plt.subplots(figsize=(8, 6))
bars4 = ax.bar(travel_data.index, travel_data.values, color=['#F44336','#FF9800','#4CAF50'], width=0.4)
ax.set_ylabel('Attrition Rate (%)')
ax.set_title('Attrition Rate by Business Travel', fontweight='bold', fontsize=13)
for bar, val in zip(bars4, travel_data.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, f'{val:.1f}%', ha='center', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart4_travel_attrition.png'), dpi=150, bbox_inches='tight')
print("Chart 4 saved")
plt.close()

# CHART 5 - Job Satisfaction vs Attrition
sat_data = df.groupby('JobSatisfaction')['Attrition_Flag'].mean() * 100
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot([1,2,3,4], sat_data.values, marker='o', linewidth=2.5, markersize=10, color='#F44336')
ax.set_xticks([1,2,3,4])
ax.set_xticklabels(['Low','Medium','High','Very High'])
ax.set_xlabel('Job Satisfaction Level')
ax.set_ylabel('Attrition Rate (%)')
ax.set_title('Job Satisfaction vs Attrition Rate', fontweight='bold', fontsize=13)
for x, val in zip([1,2,3,4], sat_data.values):
    ax.annotate(f'{val:.1f}%', (x, val), textcoords='offset points', xytext=(0,10), ha='center', fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart5_satisfaction_attrition.png'), dpi=150, bbox_inches='tight')
print("Chart 5 saved")
plt.close()

print("All 5 charts saved")
