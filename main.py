import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Video path
video_path = "./test.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read video frames
while True:
    ret, frame = cap.read()

    # Stop when video ends
    if not ret:
        break

    # Detect and track objects
    results = model.track(frame, persist=True)

    # Draw bounding boxes and tracking IDs
    annotated_frame = results[0].plot()

    # Display results
    cv2.imshow("YOLOv8 Object Tracking", annotated_frame)

    # Press Q to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
