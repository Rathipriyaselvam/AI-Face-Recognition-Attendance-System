import cv2
import os

student_name = input("Enter Student Name: ")

path = f"dataset/{student_name}"

os.makedirs(path, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

while True:

    ret, frame = camera.read()

    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):

        count += 1

        cv2.imwrite(
            f"{path}/{count}.jpg",
            frame
        )

        print(f"Saved Image {count}")

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
