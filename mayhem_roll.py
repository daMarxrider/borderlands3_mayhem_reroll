import time
import mss.tools
import numpy
import pytesseract
import pywinauto
import cv2
from PIL import ImageEnhance, ImageOps, Image
y=pywinauto.application.Application().connect(process=pywinauto.findwindows.find_element(title='Borderlands® 3  ').process_id)
mods=[]
while mod:=input('mod:'):
    mods.append(mod)
    mod = input('mod:')
monitor_number = 3
with mss.mss() as sct:
    while True:
        y.window().send_keystrokes('q')
        time.sleep(.3)
        #
        # monitor = {
        #     "top":mon['height']//2.5,
        #     "left":mon['width']//1.5,
        #     "width": mon['width']//4,
        #     "height": mon['height']//2,
        #     "mon": monitor_number,
        # }
        #
        #
        #
        # mon['height'] // 2.5
        mon = sct.monitors[monitor_number]
        h=mon['height']
        monitor = {
            "top":0,
            "left":mon['width']*2//3,
            "width": mon['width']>>2,
            "height": h,
            "mon": monitor_number,
        }
        im = numpy.asarray(sct.grab(monitor))
        dimg = ImageOps.grayscale(Image.fromarray(im))
        cimg = ImageOps.invert(dimg)
        # contrast = ImageEnhance.Contrast(cimg)
        # eimg = contrast.enhance(1)
        # sharp = ImageEnhance.Sharpness(dimg)
        # eimg = sharp.enhance(1)
        text = pytesseract.image_to_string(cimg)
        # cv2.imshow("OpenCV/Numpy normal", eimg)
        #
        # # Display the picture in grayscale
        # # cv2.imshow('OpenCV/Numpy grayscale',
        # #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
        #
        # # Press "q" to quit
        # if cv2.waitKey(25) & 0xFF == ord("q"):
        #     cv2.destroyAllWindows()
        #     break

        print(text)
        c=0
        for req in mods:
           if req.lower() in text.lower():
               c+=1
        if (c==mods.__len__() or c==4) and input('happy?(y/n)').lower()=='y':
            exit(0)
        else:
            y.window().send_chars('q')