import cv2
import numpy as np

cap = cv2.VideoCapture(0)
net = cv2.dnn.readNet("./yolov3.weights", "./yolov3.cfg")


# Colors for each object frame
colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255]]


# Importing class text files
with open("classes.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

while cap.isOpened() :
    _, frame = cap.read()
    height, width, _ = frame.shape

    # Perform object detection
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    # Draw bounding boxes on the detected objects
    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype("int")
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            
            if i < len(colors):
                color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y + 30), font, 3, color, 2)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(30) == 27:
        break



cap.release()
cv2.destroyAllWindows()
