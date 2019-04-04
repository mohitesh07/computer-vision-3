import cv2

camera_capture = cv2.VideoCapture(0)
fps = 30 # an assumption
size = (int(camera_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(camera_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

video_writer = cv2.VideoWriter('MyRecording.avi',
                               cv2.VideoWriter_fourcc('I','4','2','0'),
                               fps,
                               size)

success, frame = camera_capture.read()
numFramesRemaining = 10*fps - 1

while success and numFramesRemaining>0:
    video_writer.write(frame)
    success, frame = camera_capture.read()
    numFramesRemaining-=1
camera_capture.release()
