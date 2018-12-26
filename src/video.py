import numpy
import cv2

VIDEO_FILENAME = '/tmp/video1.mp4'
#NOTE: Above Video is owned by NATGEO. 
class VideoCV2:

    def __init__(self, src):
        # SRC can be either
        # Device Index = 0, 1, 2 depending on no. of camera
        # Name of Video File
        self.vid = cv2.VideoCapture(src)
        self.out = None
        if not self.vid.isOpened():
            print("Capture not initialized. Try running saved video")
            self.vid.open(src) # Try to open it again
            #While the Capture logic works for WebCam,
            #Open works for Saved Videos. So this code
            #handles both :)
            if not self.vid.isOpened():
                print("Neither Capture nor saved Video works!!")

    def read_frames(self):
        while(True):
            ret, frame = self.vid.read() #Read Frames 1-by-1
            if not ret:
                break    # self.vid.read() is False at the End of Video
            converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', converted_frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'): # For a stream video, press 'q' to stop
                break

    def close(self):
        # All sources are released simultaneously at the end
        self.vid.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()

    def get_video_property(self):
        # More information of this in the doc folder
        for id in range(0,19):
            print(self.vid.get(id))

    def write_frames(self):
        # fourcc is a 4Byte code for codec used to save the video
        # videowriter has following arguments:Name of Dest File, FourCC code,
        # FPS, Frame Size and isColor option
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('../Pictures/video1.avi', fourcc, 30, (640, 480))
        while(True):
            ret, frame = self.vid.read() #Read Frames 1-by-1
            if not ret:
                break    # self.vid.read() is False at the End of Video
            #converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            converted_frame = cv2.flip(frame, 0) # Flip in Vertical direction ( 0 degrees)
            self.out.write(converted_frame)
            # I found an issue wherein GRAYSCALE videos were not being saved, due to DEPTH error,
            # so I skipped it.
            cv2.imshow('frame', converted_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): # For a stream video, press 'q' to stop
                break
 

# Note: My OpenCV didnt have support for ffmpeg earlier, so couldnt work on mp4.
# It started working after H264 codecs downloaded, so if it fails, try it :)
# https://stackoverflow.com/questions/47112642/permanent-fix-for-opencv-videocapture
video = VideoCV2(0)
video.read_frames()
video.get_video_property()
video.write_frames()
video.close()
video = VideoCV2(VIDEO_FILENAME)
video.read_frames()
video.get_video_property()
video.close()
