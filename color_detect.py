#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:10:55 2020

@author: josef
"""

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

while True:
    
    _, frame = capture.read()
    #convert to hsv 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    Unio_2_colors = cv2.add(red, green)
    all_colors = cv2.add(Unio_2_colors, blue)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red Green Blue", all_colors)



    key = cv2.waitKey(1)
    if key == 27:
        break