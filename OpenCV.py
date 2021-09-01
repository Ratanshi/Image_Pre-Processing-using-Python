#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Import OpenCV
import cv2
print("Package Imported")


# In[4]:


#Read Images , Using a function imread and show using imshow
import cv2
img = cv2.imread("Image Path")
cv2.imshow("Output",img)
cv2.waitKey(0)


# In[ ]:


#Read Videos
import cv2
cap = cv2.VideoCapture("Video Path")
#Video is a sequence of images , Hence a while loop is used to display the images.

while True:
#success here has a boolean value true or false   
     success, img = cap.read()
     cv2.imshow("Video" ,img)
#And operation is performed between waitKey and 0xFF and the value is checked for ord('q')
     if cv2.waitKey(100) & 0xFF == ord('q'): #0-255
  #        10010011     0b11111111          8 bits      
           break


# In[ ]:


#Read Videos
import cv2
cap = cv2.VideoCapture(0) #Webcam input windows(0) Linux(-1)
cap.set(3,640)
cap.set(10,100) #cap.set(id,value)  id 10 is for brightness
#Video is a sequence of images , Hence a while loop is used to display the images.

while True:
#success here has a boolean value true or false   
     success, img = cap.read()
     cv2.imshow("Video" ,img)
#And operation is performed between waitKey and 0xFF and the value is checked for ord('q')
     if cv2.waitKey(100) & 0xFF == ord('q'): #0-255
  #        10010011     0b11111111          8 bits      
           break


# In[2]:


#convert to gray
import cv2

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)


# In[4]:


#convert to gray and blur
import cv2

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #(odd,odd)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)


# In[10]:


#Edge Detection using Canny
import cv2

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #(odd,odd)
imgCanny = cv2.Canny(img,100,100)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)

cv2.waitKey(0)


# In[18]:


#Dialation and erosion using Canny 
import cv2
import numpy as np

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
kernel = np.ones((5,5),np.uint8)
#Here we define Kernel , where we define a matrix of (5,5) of all values as 1 (np.one)
#And parameter of type unsigned int of 8 bytes 

imgCanny = cv2.Canny(img,100,100)
imgDia = cv2.dilate(imgCanny , kernel , iterations = 5)
imgEro = cv2.erode(imgDia , kernel , iterations = 4)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialated Image", imgDia)
cv2.imshow("Erosion Image", imgEro)
cv2.waitKey(0)


# In[19]:


#Dimensions
import cv2
import numpy as np

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
print(img.shape)


# In[24]:


#Resizing
import cv2
import numpy as np

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

cv2.imshow(" Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)


# In[25]:


#Cropping

import cv2
import numpy as np

img=cv2.imread("C:/Users/HP/Desktop/a.webp")

imgCrop = img[0:200,200:500]

cv2.imshow(" Image", img)
cv2.imshow("Cropped Image", imgCrop)
cv2.waitKey(0)


# In[ ]:


import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print (img)
img[:] = 255,255,255

cv2.imshow(" Image", img)
cv2.waitKey(0)


# In[40]:


#Draw A Line
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(300,300),(255,0,0),3)
# (image_name ,  starting point , ending point ,color , Thickness)
#cv2.line(img.shape[1],image.shape[0],(255,0,0),3)
              # Widht , Height 
cv2.imshow("Image", img)
cv2.waitKey(0)


# In[43]:


#Draw A Rectangle
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(0,0),(250,350),(255,0,0),cv2.FILLED)
# (image_name ,  starting point , ending point ,color , Thickness/Filled shape)


cv2.imshow("Image", img)
cv2.waitKey(0)


# In[45]:


#Draw A Circles
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.circle(img,(400,50),30,(255,0,255),cv2.FILLED)
# (image_name , center ,radius ,color , Thickness/Filled shape)

cv2.imshow("Image", img)
cv2.waitKey(0)


# In[48]:


#Text on images
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.putText(img," OpenCV ",(200,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,100,0),1)
# (image_name , Text ,starting point ,font, scale(Font_size), color , thickness(Boldness))

cv2.imshow("Image", img)
cv2.waitKey(0)


# In[49]:


#Warp Percpective to get Birds eye view


# In[52]:


#Joining of images
import cv2
import numpy as np

img=cv2.imread("C:/Users/HP/Desktop/a.webp")
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)


# In[56]:


#convert to Hue Saturated Value Image , Creating trackbars;
import cv2

img=cv2.imread("C:/Users/HP/Desktop/a.webp")

#Creating Trackbars for chaninging saturation value
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 650,250)


imgHSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

cv2.imshow("Gray Image", imgHSV)
cv2.waitKey(0)


# In[ ]:





# In[ ]:




