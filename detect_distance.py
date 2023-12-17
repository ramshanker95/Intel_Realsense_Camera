import cv2
import numpy as np
from realsense_depth import *
import Jetson.GPIO as GPIO
# from text_finder import *
import time
import os ,argparse
import threading
# from pytesseract import pytesseract
from PIL import Image


dc = DepthCamera()

ap=argparse.ArgumentParser()

ap.add_argument("-p","--pre_processor",
				default="thresh",
				help="the preprocessor usage")
args=vars(ap.parse_args())

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

l_obj = 17
r_obj = 27
c_obj = 22
# Set up the GPIO pin as an output
GPIO.setup(l_obj, GPIO.OUT)
GPIO.setup(r_obj, GPIO.OUT)
GPIO.setup(c_obj, GPIO.OUT)
# Initialize Camera Intel Realsense
GPIO.output(l_obj, GPIO.LOW)
GPIO.output(r_obj, GPIO.LOW)
GPIO.output(c_obj, GPIO.LOW)


def lidar_camra():
    while True:
        try:
            turn_1 = True
            turn_2 = True
            turn_3 = True
            turn_4 = True
            turn_5 = True
            turn_6 = True
            turn_7 = True
            turn_8 = True
            roi_result = np.ones((8,8))
            ret, depth_frame, color_frame = dc.get_frame()
            # print(depth_frame.shape)
            g = 60
            for xind, x in enumerate(range(100, 580, g)):
                for yind, y in enumerate(range(0, 480, g)):
                    roi_result[xind][yind] = np.average(depth_frame[x:x+g, y:y+g])

            # print(roi_result.round(2))
            data_turn = roi_result.round(2)>600
            # print(data_turn)
            for row in range(8):
                if data_turn[row][0]==False:
                    turn_1 = False
                if data_turn[row][1]==False:
                    turn_2 = False
                if data_turn[row][2]==False:
                    turn_3 = False
                if data_turn[row][3]==False:
                    turn_4 = False
                if data_turn[row][4]==False:
                    turn_5 = False
                if data_turn[row][5]==False:
                    turn_6 = False
                if data_turn[row][6]==False:
                    turn_7 = False
                if data_turn[row][7]==False:
                    turn_8 = False
                    
                    
            if (turn_1 and turn_2 and turn_3 and turn_4 and turn_5 and turn_6 and turn_7 and turn_8):
                GPIO.output(l_obj, GPIO.LOW)
                GPIO.output(r_obj, GPIO.LOW)
                GPIO.output(c_obj, GPIO.LOW)
                print("forward")

            elif((not turn_1 and turn_2 and turn_3 and turn_4 and turn_5 and turn_6 and turn_7 and turn_8) or (not turn_1 and not turn_2 and turn_3 and turn_4 and turn_5 and turn_6 and turn_7 and turn_8) or 
                (not turn_1 and not turn_2 and not turn_3 and turn_4 and turn_5 and turn_6 and turn_7 and turn_8)or (not turn_1 or not turn_2 or not turn_3 and turn_4 and turn_5 and turn_6 and turn_7 and turn_8)):
                # time.sleep(5)
                GPIO.output(l_obj, GPIO.HIGH)
                GPIO.output(r_obj, GPIO.LOW)
                GPIO.output(c_obj, GPIO.LOW)
                print("obj_Left side ")

            elif((turn_1 and turn_2 and turn_3 and turn_4 and turn_5 and turn_6 and turn_7 and not turn_8) or (turn_1 and turn_2 and turn_3 and turn_4 and turn_5 and turn_6 and not turn_7 and not turn_8) or 
                (turn_1 and turn_2 and turn_3 and turn_4 and not turn_5 and not turn_6 and not turn_7 and not turn_8) or (turn_1 and turn_2 and turn_3 and turn_4 or not turn_5 or not turn_6 or not turn_7 or not turn_8)):
                # time.sleep(5)
                GPIO.output(r_obj, GPIO.HIGH)
                GPIO.output(l_obj, GPIO.LOW)
                GPIO.output(c_obj, GPIO.LOW)
                print("obj_Right side ")

            # elif((turn_1 and turn_2 and not turn_3 and turn_4 and turn_5 and turn_6 and turn_7) or (turn_1 and turn_2 and turn_3 and not turn_4 and turn_5 and turn_6 and turn_7) or 
            #     (turn_1 and turn_2 and turn_3 and turn_4 and not turn_5 and turn_6 and turn_7) or (turn_1 and turn_2 and not turn_3 and not turn_4 and turn_5 and turn_6 and turn_7) or 
            #     (turn_1 and turn_2 and turn_3 and not turn_4 and not turn_5 and turn_6 and turn_7) or (turn_1 and turn_2 and not turn_3 and not turn_4 and not turn_5 and turn_6 and turn_7)):
            #     GPIO.output(c_obj, GPIO.HIGH)
            #     print("obj_Center side ")

            else:
                # time.sleep(5)
                # GPIO.output(c_obj, GPIO.HIGH)
                # GPIO.output(r_obj, GPIO.LOW)
                # GPIO.output(l_obj, GPIO.LOW)
                print("obj_Center side ")
                GPIO.output(l_obj, GPIO.HIGH)
                GPIO.output(r_obj, GPIO.HIGH)
                GPIO.output(c_obj, GPIO.HIGH)
                # print("stop")
            print("---------------")
            # cv2.imshow("depth frame", depth_frame[160:640,20:440])
            # cv2.imshow("Color frame", color_frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        except KeyboardInterrupt:
            dc.release()
            print("Done")
            break


if __name__ == "__main__":
    lidar_camra()
    # creating threads
    # t1 = threading.Thread(target=lidar_camra, name='t1')
    # t2 = threading.Thread(target=text_reader, name='t2')
 
    # # starting threads
    # t1.start()
    # t2.start()
 
    # # wait until all threads finish
    # t1.join()
    # t2.join()