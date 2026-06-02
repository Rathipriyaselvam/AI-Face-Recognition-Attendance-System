import pandas as pd

df = pd.read_csv(
    "attendance/attendance.csv"
)

df.to_excel(
    "reports/attendance_report.xlsx",
    index=False
)

print("Report Generated")