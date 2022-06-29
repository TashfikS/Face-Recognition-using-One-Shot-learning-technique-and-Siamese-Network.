from itertools import count
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

count = 0

while True:
    ret, frame = cam.read()
    frame = frame[120:120+250,200:200+250, :]
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "C:/Users/User/Desktop/data/positive/{}.jpg".format(count)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        count+=1
cam.release()

cv2.destroyAllWindows()