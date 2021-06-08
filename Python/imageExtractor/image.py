import cv2
import os
import numpy as np

# Program To Read video
# and Extract Frames
import cv2
  
# Function to extract frames
def FrameCapture(path):
      
    # Path to video file
    vidObj = cv2.VideoCapture(path)
  
    # Used as counter variable
    count = 0
    avoidTrans = 0
    # checks whether frames were extracted
    success = 1
    prev = []
    while success:
        avoidTrans +=1
        success, image = vidObj.read()
        if avoidTrans < 27:
          #print(avoidTrans)
          continue
        avoidTrans = 0        
        if len(prev) > 0:
          x = len(image)
          y = len(image[0])
          pixelSimilarity = 0
          b=0
          for img in image:  
            c = 0
            red = 0
            green = 1
            blue = 2
            
            for pixel in img:
              prevpixel = prev[b][c]
              #print(c,avoidTrans,pixel[red],prevpixel[red])
              if pixel[red] != prevpixel[red] or pixel[green] != prevpixel[green] or pixel[blue] != prevpixel[blue]:
                pixelSimilarity += 1
              
              c+=1
            b+=1
          pd = pixelSimilarity/(x*y)
          #print(pixelSimilarity,x*y,x,y,pd,avoidTrans)
          if pd > 0.8:
            #print(pixelSimilarity,x*y,x,y,pd,avoidTrans)
            print(pd)
            cv2.imwrite("images/DiffFrame%d.jpg" % count, image)    
        # Saves the frames with frame-count
        prev = image
  
        count += 1
  
# Driver Code
if __name__ == '__main__':
  
    # Calling the function
   FrameCapture("video.mp4")
