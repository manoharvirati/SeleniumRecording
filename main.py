#import libraries
from selenium import webdriver
import pyautogui
import cv2
import numpy as np
import time

#input location
location=input("Address or Coordinates : ")

resolution=(1920,1080)
codec=cv2.VideoWriter_fourcc(*"XVID")

#specify output filename
filename="Recording.mp4"

#specify frame rate
fps=7.0
out=cv2.VideoWriter(filename,codec,fps,resolution)

#path to web driver(download according to your chrome version)
driver=webdriver.Chrome(executable_path=r"C:\Users\Danger\Downloads\chromedriver_win32\chromedriver")

#url of google earth customized
url="https://earth.google.com/web/search/"+location+"/"

#opening browser
driver.maximize_window()
driver.get(url)
time.sleep(10)
cv2.namedWindow("Live",cv2.WINDOW_NORMAL)

#resize the window
cv2.resizeWindow("Live",480,270)
b
while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Live',frame)

    #Stop recording when we press 'q'
    if cv2.waitKey(1)==ord('q'):
        breakb
out.release()

#destroy all windows
cv2.destroyAllWindows()
