import numpy
import cv2
import subprocess as sp

pipe = sp.Popen(["ffmpeg", "-video_size", "1024x768",
                                    "-framerate", "25"
                                    "-f", "x11grab",
                                    "-i", ":0.0",
                                    "-f", "image2pipe"
                                    "-pix_fmt", "rgb24",
                                    "-vcodec", "rawvideo",
                                    "-"],
                                    stdin=sp.PIPE, stdout=sp.PIPE)

while(True):
    raw_image = pipe.stdout.read(1024*768*3) # read 420*360*3 bytes (= 1 frame)
    mat =  numpy.fromstring(raw_image, dtype='uint8')
    #print raw_image

    # Our operations on the frame come here
"""gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the resulting frame
cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the
# capture
cv2.destroyAllWindows()"""
