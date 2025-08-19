import cv2
import numpy as np


def get_limits(color):
    c = np.uint8([[color]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsv[0][0][0]

    if hue >= 165:
        lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upper = np.array([180, 255, 255], dtype=np.uint8)

    elif hue <= 15:
        lower = np.array([0, 100, 100], dtype=np.uint8)
        upper = np.array([hue + 10, 255, 255], dtype=np.uint8)

    else:
        lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upper = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lower, upper


z = [0, 255, 255]


def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        low, up = get_limits(color=z)

        mask = cv2.inRange(hsvImg, low, up)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cont in contours:
            area = cv2.contourArea(cont)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cont)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("pupu", mask)
        cv2.imshow("pupupu", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
