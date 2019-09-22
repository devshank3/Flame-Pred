import numpy as np
import cv2
import time
import xlsxwriter

color=(210,0,0)
thickness=1

workbook = xlsxwriter.Workbook('C:\\Users\\shank\\Desktop\\PS 6 Flame\\ethanolheat.xlsx')
worksheet = workbook.add_worksheet()

row=0;
col=0;
worksheet.write(row, col,     'height')
worksheet.write(row, col + 1, 'side')
row += 1
cap = cv2.VideoCapture("C:\\Users\\shank\\Desktop\\PS 6 Flame\\Ethanol-1.mp4");
while(True):
    # Capture two frames
    ret, frame1 = cap.read()  # first image
    time.sleep(1/20)          # slight delay
    ret, frame2 = cap.read()  # second image 
    img1 = cv2.absdiff(frame1,frame2)  # image difference

    
    
    # get threshold image
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(21,21),0)
    ret,thresh = cv2.threshold(blur,220,250,cv2.THRESH_OTSU)
    
    # combine frame and the image difference
    img2 = cv2.addWeighted(frame1,0.2,img1,0.8,0)
    
    # get contours and set bounding box from contours
    img3, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        for c in contours:
            rect = cv2.boundingRect(c)
            height, width = img3.shape[:2]            
            if rect[2] > 0.2*height and rect[2] < 0.7*height and rect[3] > 0.2*width and rect[3] < 0.7*width: 
                x,y,w,h = cv2.boundingRect(c)            # get bounding box of largest contour
                img4=cv2.drawContours(img2, c, -1, color, thickness)
                
                img5 = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),1)# draw red bounding box in img
                biggest = np.amax(img2)
                print(w)
                
                print(biggest)
                
                if (y+h)>270:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    img2=cv2.putText(img2,'LEFT',(130,130), font, 1,(255,255,255),2,cv2.LINE_AA)
                    worksheet.write(row, col,     w)
                    worksheet.write(row, col + 1, 'left')
                    row += 1
                elif y<100:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    img2=cv2.putText(img2,'RIGHT',(130,130), font, 1,(255,255,255),2,cv2.LINE_AA)
                    worksheet.write(row, col,     w)
                    worksheet.write(row, col + 1, 'Right')
                    row += 1
                elif (y+h)<270 and y>100 and x<240:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    img2=cv2.putText(img2,'high straight',(130,130), font, 1,(255,255,255),2,cv2.LINE_AA)
                    worksheet.write(row, col,     w)
                    worksheet.write(row, col + 1, 'high')
                    row += 1
                elif (y+h)<270 and y>100:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    img2=cv2.putText(img2,'CONTAINED',(130,130), font, 1,(255,255,255),2,cv2.LINE_AA)
                    worksheet.write(row, col,     w)
                    worksheet.write(row, col + 1, 'Contained')
                    row += 1


                    
            else:
                img5=img2
                

    else:
        img5=img2

        
    img2 = cv2.rectangle(img2,(240,100),(460,270),(0,255,0),2)
    (h,w)=img2.shape[:2]
    center=(w/3,h/3)
    angle= -90
    scale= 1
    m=cv2.getRotationMatrix2D(center, angle,scale)
    img2=cv2.warpAffine(img2,m,(h,w))
    
   
    
    # Display the resulting image
    cv2.imshow('Motion Detection by Image Difference',img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
        
# When everything done, release the capture
workbook.close()
cap.release()
cv2.destroyAllWindows()
