import cv2


OUTPUT_FILE = "output.avi"
FPS = 20.0
VIDEO_SIZE = (640,480)

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(OUTPUT_FILE , fourcc , FPS , VIDEO_SIZE)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)


    out.write(frame)

    cv2.imshow("live" , frame)

    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()


