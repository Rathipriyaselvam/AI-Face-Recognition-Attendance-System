import pandas as pd
from datetime import datetime

def mark_attendance(name, dept):

    now = datetime.now()

    time = now.strftime("%H:%M:%S")

    date = now.strftime("%d-%m-%Y")

    df = pd.read_csv(
        "attendance/attendance.csv"
    )

    today = df[
        (df["Name"] == name)
        &
        (df["Date"] == date)
    ]

    if len(today) == 0:

        new_row = {
            "Name": name,
            "Department": dept,
            "Time": time,
            "Date": date,
            "Status": "Present"
        }

        df.loc[len(df)] = new_row

        df.to_csv(
            "attendance/attendance.csv",
            index=False
        )

        print("Attendance Marked")