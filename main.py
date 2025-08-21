import cv2
import numpy as np
from limits import get_ranges

color = [0, 255, 255]


def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Получаем диапазоны
        ranges = get_ranges(color, tol=15, s_min=80, v_min=80)

        # Строим маску (две маски для красного)
        mask = np.zeros(hsv_frame.shape[:2], dtype=np.uint8)

        for low, up in ranges:
            mask |= cv2.inRange(hsv_frame, low,
                                up)  # накладываем маски (из-за красного цвета, который состоит из двух диапозонов)

        # Поиск контуров
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cont in contours:
            if cv2.contourArea(cont) > 500:  # фильтр
                x, y, w, h = cv2.boundingRect(cont)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("pupupu.", mask)
        cv2.imshow("pupuppupu.", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
