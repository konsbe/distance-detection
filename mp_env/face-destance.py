import time
from cv2 import cv2,CAP_V4L

cap = cv2.VideoCapture(1)

def test_open_cam():
    connected_cam = []
    for port in range(0, 10):
        try:
            cam = cv2.VideoCapture(port)
            if cam.isOpened():
                connected_cam.append(port)
                print(port)
            cam.release()
            cv2.destroyAllWindows()
        except:
            cam.release()
            cv2.destroyAllWindows()
    print(f'=> list of found cameras: {connected_cam}', port)
    return(connected_cam)

test_open_cam()

while True:
    success, frame = cap.read()

    # Display the resulting frame
    if success:
        cv2.imwrite(time.strftime("%Y%m%d-%H%M%S"), frame)
    cv2.startWindowThread()
    cv2.namedWindow("frame")
    cv2.imshow("frame", frame)
    cv2.waitKey()
        # cap.release()
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    cap.release()
    cv2.destroyAllWindows()

# When everything done, release the capture
    # cv2.destroyAllWindows()