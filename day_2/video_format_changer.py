import cv2
video_ip = cv2.VideoCapture('myInputVid.avi')

# finding the frames per second (fps)
fps = video_ip.get(cv2.CAP_PROP_FPS)

# finding the size of the video frame
size = (int(video_ip.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video_ip.get(cv2.CAP_PROP_FRAME_HEIGHT)))

video_writer = cv2.VideoWriter('myOutputVid.avi',
                               cv2.VideoWriter_fourcc('I','4','2','0'),
                               fps,
                               size)

success, frame = video_ip.read()
while success:  #Loop until no more frames are left
    video_writer.write(frame)
    success, frame = video_ip.read()
    
