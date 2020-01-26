from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import numpy as np
import cv2
import time
import picamera
import datetime as dt
import board
import busio
import adafruit_sgp30
import adafruit_lsm9ds1
<<<<<<< HEAD

=======
import csv
from datetime import datetime




f = open("accel.csv", "w", newline="")
c=csv.writer(f)
start = time.monotonic()
>>>>>>> 66d1ad9646eca1d0e9d9ddc57e5622adefec8ba1
xyz = 5
x = 0
y = 0
z = 0

filename = 'video.avi' # .avi .mp4
frames_per_seconds = 24.0
my_res = (640, 480) #'480p' # 1080p


cap = cv2.VideoCapture(0)

video_type_cv2 = cv2.VideoWriter_fourcc(*'XVID')
save_path = os.path.join(filename)

out = cv2.VideoWriter('video.avi', video_type_cv2, frames_per_seconds, my_res)

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

# Create library object on our I2C port
<<<<<<< HEAD
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)
=======
#sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
#print("SGP30 serial #", [hex(i) for i in sgp30.serial])
#sgp30.iaq_init()
#sgp30.set_iaq_baseline(0x8973, 0x8aae)
>>>>>>> 66d1ad9646eca1d0e9d9ddc57e5622adefec8ba1

elapsed_sec = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
<<<<<<< HEAD

=======
    now = datetime.now()
    c.writerow([time.monotonic(), accel_x, accel_y, accel_z, temp])
>>>>>>> 66d1ad9646eca1d0e9d9ddc57e5622adefec8ba1
    # Print values.
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(accel_x, accel_y, accel_z))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(mag_x, mag_y, mag_z))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    print('Temperature: {0:0.3f}C'.format(temp))
    
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Draw framerate in corner of frame
<<<<<<< HEAD
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    
    #cv2.putText(frame,str(xyz),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(51, 51, 0),2,cv2.LINE_AA)
    cv2.putText(frame,str(sgp30.eCO2),(30,90),cv2.FONT_HERSHEY_SIMPLEX,1,(51, 51, 0),2,cv2.LINE_AA)
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    #time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        #elapsed_sec = 0
        print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
              % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
#     print(getVal())
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
=======
    #print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    
    cv2.putText(frame,now.strftime("%H:%M:%S"),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(51, 51, 0),2,cv2.LINE_AA)
    #cv2.putText(frame,str(sgp30.eCO2),(30,90),cv2.FONT_HERSHEY_SIMPLEX,1,(51, 51, 0),2,cv2.LINE_AA)
    #print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    #time.sleep(1)
    elapsed_sec += 1
    out.write(frame)
    # Display the resulting frame
    #cv2.imshow('frame',frame)
>>>>>>> 66d1ad9646eca1d0e9d9ddc57e5622adefec8ba1
    
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
<<<<<<< HEAD
=======
f.close()
>>>>>>> 66d1ad9646eca1d0e9d9ddc57e5622adefec8ba1