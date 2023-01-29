import cv2


def capture():
    cap = cv2.VideoCapture(0)
    while cap.isOpened() :
        ret, frame = cap.read()
        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_RGB2BGR)

        # cv2.imshow("Camera", frame)
        
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

