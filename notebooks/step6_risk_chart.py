import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(base_dir, 'data', 'hr_cleaned.csv'))
output_dir = os.path.join(base_dir, 'output')

median_income = df["MonthlyIncome"].median()
df["risk_overtime"] = (df["OverTime"] == "Yes").astype(int)
df["risk_low_salary"] = (df["MonthlyIncome"] < median_income).astype(int)
df["risk_travel"] = (df["BusinessTravel"] == "Travel_Frequently").astype(int)
df["risk_score"] = df["risk_overtime"] + df["risk_low_salary"] + df["risk_travel"]

risk_analysis = df.groupby("risk_score")["Attrition_Flag"].agg(
    Total="count",
    Left="sum",
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

colors = ["#4CAF50", "#FF9800", "#FF5722", "#F44336"]
bars = axes[0].bar(
    ["0 Risk Factors", "1 Risk Factor", "2 Risk Factors", "3 Risk Factors"],
    risk_analysis["Attrition_Rate"],
    color=colors, edgecolor="white", width=0.5
)
axes[0].set_ylabel("Attrition Rate (%)", fontsize=12)
axes[0].set_title("Attrition Rate Increases With Each Risk Factor\n(Overtime + Low Salary + Frequent Travel)", fontweight="bold", fontsize=12)
for bar, val, total, left in zip(bars, risk_analysis["Attrition_Rate"], risk_analysis["Total"], risk_analysis["Left"]):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f"{val}%\n({left}/{total})", ha="center", fontsize=10, fontweight="bold")
axes[0].set_ylim(0, 80)
axes[0].axhline(y=16.1, color="black", linestyle="--", linewidth=1.5, label="Company Average 16.1%")
axes[0].legend(fontsize=10)

dept_risk3 = df[df["risk_score"] >= 2].groupby(["Department", "risk_score"])["Attrition_Flag"].agg(
    Total="count",
    Attrition_Rate=lambda x: round(x.mean() * 100, 2)
).reset_index()

departments = dept_risk3["Department"].unique()
risk_scores = [2, 3]
x = range(len(departments))
width = 0.3
colors2 = ["#FF5722", "#F44336"]

for i, score in enumerate(risk_scores):
    data = dept_risk3[dept_risk3["risk_score"] == score]
    rates = []
    for dept in departments:
        row = data[data["Department"] == dept]
        rates.append(row["Attrition_Rate"].values[0] if len(row) > 0 else 0)
    axes[1].bar([xi + i*width for xi in x], rates, width=width,
                label=f"Risk Score {score}", color=colors2[i], edgecolor="white")

axes[1].set_xticks([xi + width/2 for xi in x])
axes[1].set_xticklabels(departments, fontsize=10)
axes[1].set_ylabel("Attrition Rate (%)", fontsize=12)
axes[1].set_title("High Risk Employees by Department\n(Risk Score 2 and 3 Only)", fontweight="bold", fontsize=12)
axes[1].legend(fontsize=10)
axes[1].set_ylim(0, 110)

plt.suptitle("Combined Risk Factor Analysis: Who Is Most Likely To Leave?\nEmployees with Overtime + Low Salary + Frequent Travel", 
             fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "chart6_risk_score_analysis.png"), dpi=150, bbox_inches="tight")
print("Chart saved successfully")
plt.close()
