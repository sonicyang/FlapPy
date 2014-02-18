import numpy as np
import cv2

drawing = False # true if mouse is pressed
ix,iy = -1,-1
ex,ey = -1,-1

def nothing(x):
        pass

# mouse callback function
def selectROI(event,x,y,flags,param):
    global ix,iy,drawing,mode,ex,ey

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        ex,ey = x+1,y+1

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ex,ey = x,y
        #cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)


# Create a black image, a window
cv2.namedWindow('image')
cv2.namedWindow('image2')

# create trackbars for HSV change
cv2.createTrackbar('HL','image',0,180,nothing)
cv2.createTrackbar('SL','image',0,255,nothing)
cv2.createTrackbar('VL','image',0,255,nothing)
cv2.createTrackbar('HH','image',0,180,nothing)
cv2.createTrackbar('SH','image',0,255,nothing)
cv2.createTrackbar('VH','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

# create call back for Selecting ROI on image window
cv2.setMouseCallback('image2',selectROI)

cap = cv2.VideoCapture(1)

while(True):
        # get current positions of four trackbars
        hl = cv2.getTrackbarPos('HL','image')
        sl = cv2.getTrackbarPos('SL','image')
        vl = cv2.getTrackbarPos('VL','image')
        hh = cv2.getTrackbarPos('HH','image')
        sh = cv2.getTrackbarPos('SH','image')
        vh = cv2.getTrackbarPos('VH','image')
        
        s = cv2.getTrackbarPos(switch,'image')

        # Capture frame-by-frame
        ret, frame = cap.read()

        gameroi = frame[50:700,0:400]

        frame = cv2.blur(frame,(5,5))
        
        piperoi = gameroi[0:768,300:400]
        
        piperoi_hsv = cv2.cvtColor(piperoi,cv2.COLOR_BGR2HSV) 
    
        """lower_pipe = np.array([hl,sl,vl], dtype=np.uint8)
        upper_pipe = np.array([hh,sh,vh], dtype=np.uint8)"""
        lower_pipe = np.array([35,80,68], dtype=np.uint8)
        upper_pipe = np.array([77,208,152], dtype=np.uint8)
        
        piperoi_mask = cv2.inRange(piperoi_hsv, lower_pipe, upper_pipe)
        
        M = cv2.moments(piperoi_mask)
        area = M['m00']
        if(area > 100000):
            cent_x = int(M['m10']/M['m00'])
            cent_y = int(M['m01']/M['m00'])
            acc_cent_y = 400 - cent_y
            cv2.line(gameroi,(0,acc_cent_y),(399,acc_cent_y),(0,0,255),5)
            print(cent_x,cent_y)
        cv2.imshow('image3',piperoi_mask)


        cv2.imshow('image2',gameroi)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

