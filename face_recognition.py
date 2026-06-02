from deepface import DeepFace
import cv2
import pandas as pd
from datetime import datetime
import os

camera = cv2.VideoCapture(0)

attendance_marked = False

while True:

    ret, frame = camera.read()

    cv2.imshow("Recognition", frame)

    cv2.imwrite("temp.jpg", frame)

    try:

        result = DeepFace.find(
            img_path="temp.jpg",
            db_path="dataset",
            enforce_detection=False
        )

        if len(result) > 0 and len(result[0]) > 0:

            best_match = result[0].iloc[0]

            identity_path = best_match["identity"]

            name = identity_path.split("/")[1]

            print(f"Recognized: {name}")

            if not attendance_marked:

                now = datetime.now()

                time = now.strftime("%H:%M:%S")
                date = now.strftime("%d-%m-%Y")

                attendance = pd.read_csv(
                    "attendance/attendance.csv"
                )

                attendance.loc[len(attendance)] = [
                    name,
                    "AI&DS",
                    time,
                    date,
                    "Present"
                ]

                attendance.to_csv(
                    "attendance/attendance.csv",
                    index=False
                )

                print("Attendance Marked!")

                attendance_marked = True

                break

    except Exception as e:
        print(e)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()