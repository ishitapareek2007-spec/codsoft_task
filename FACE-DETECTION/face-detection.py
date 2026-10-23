import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades +
                             "haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
