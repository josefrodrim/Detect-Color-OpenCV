#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:10:55 2020

@author: josef
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)


def drawBorder(mask,color):
  
  contornos, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 3000:
      M = cv2.moments(c)
      if (M["m00"]==0): M["m00"]=1
      x = int(M["m10"]/M["m00"])
      y = int(M['m01']/M['m00'])
      newContorn = cv2.convexHull(c)
      
      cv2.circle(frame,(x,y),7,(0,255,0),-1)
      
      font = cv2.FONT_HERSHEY_SIMPLEX
      
      if color == (0,0,255): 
          cv2.putText(frame,'red',(x+10,y), font , 0.75,(0,0,255),1,cv2.LINE_AA)
      if color == (255,0,0): 
          cv2.putText(frame,'blue',(x+10,y), font , 0.75,(255,0,0),1,cv2.LINE_AA)
      if color == (50,205,50): 
          cv2.putText(frame,'green',(x+10,y), font , 0.75,(50,205,50),1,cv2.LINE_AA)
      
      cv2.drawContours(frame, [newContorn], 0, color, 3)


while True:
    
    _, frame = cap.read()
    #convert to hsv 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    red_2 = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    blue_2 = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    green_2 = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
    
    Unio_2_colors = cv2.add(red, green)
    all_colors = cv2.add(Unio_2_colors, blue)
    
    drawBorder(red_2,(0,0,255))
    drawBorder(blue_2,(255,0,0))
    drawBorder(green_2,(50,205,50))
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red Green Blue", all_colors)


    key = cv2.waitKey(1)
    if key == 27:
        break