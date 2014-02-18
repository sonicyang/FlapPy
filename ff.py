import subprocess as sp
import numpy

pipe = sp.Popen(["avconv", "-video_size", "100x100",
                       "-re","-an",
                       #"-b","500k"
                       "-f", "x11grab",
                       "-i", ":0.0",
                       "-r", "25",
                       "-f", "image2pipe",
                       "-pix_fmt", "rgb24",
                       "-vcodec", "rawvideo", "-"],
                       stdin = sp.PIPE, stdout = sp.PIPE)

raw_image = pipe.stdout.read(100*100*3) # read 420*360*3 bytes (= 1 frame)
print len(raw_image)
#image =  numpy.fromstring(raw_image, dtype='uint8').reshape((360,420,3))


