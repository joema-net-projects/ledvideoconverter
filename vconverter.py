import cv2
import textwrap

wrapper = textwrap.TextWrapper(width=70)

#Height and width of video to resize to.
width = 48
height = 36

cap = cv2.VideoCapture('NAME OF VIDEO HERE')
file = open("NAME OF TEXT.TXT",'w') 
 
while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteFrame) = cv2.threshold(b, 127, 255, cv2.THRESH_BINARY)
        c = cv2.resize(blackAndWhiteFrame,(width,height), interpolation = cv2.INTER_AREA)
        (h, d) = cv2.threshold(c, 127, 255, cv2.THRESH_BINARY)
        e = cv2.bilateralFilter(d,2,75,75)
            
        for i in range(height):
            for j in range(width):
                if e[i][j] > 205:
                    e[i][j] = 255
                elif e[i][j] < 50:
                    e[i][j] = 0 
            print(str(wrapper.wrap(str(e[i]))).replace("[","").replace("]","").replace("'","").replace(",","").lstrip().rstrip()) #Comment this line to remove terminal output
            file.write(str(wrapper.wrap(str(e[i]))).replace("[","").replace("]","").replace("'","").replace(",","").lstrip().rstrip())
            file.write("\n")
    else:
        break
    
file.close()
cap.release()
cv2.destroyAllWindows()