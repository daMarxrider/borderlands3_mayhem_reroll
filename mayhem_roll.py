import time
import mss.tools
import numpy
import pytesseract
import pywinauto
from PIL import ImageEnhance, ImageOps, Image
y=pywinauto.application.Application().connect(process=pywinauto.findwindows.find_element(title='Borderlands® 3  ').process_id)
mods=[]
while mod:=input('mod:'):
    mods.append(mod)
    mod = input('mod:')
monitor_number = 3
time.sleep(5)
with mss.mss() as sct:
    while True:
        mon = sct.monitors[monitor_number]
        monitor = {
            "top": mon["top"] + 250,
            "left": mon["left"] + 2000,
            "width": 1500,
            "height": 1500,
            "mon": monitor_number,
        }
        im = numpy.asarray(sct.grab(monitor))
        dimg = ImageOps.grayscale(Image.fromarray(im))
        cimg = ImageOps.invert(dimg)
        contrast = ImageEnhance.Contrast(dimg)
        eimg = contrast.enhance(1)
        sharp = ImageEnhance.Sharpness(dimg)
        eimg = sharp.enhance(1)
        text = pytesseract.image_to_string(eimg)
        print(text)
        c=0
        for req in mods:
           if req.lower() in text.lower():
               c+=1
        if (c==mods.__len__() or c==4) and input('happy?(y/n)').lower()=='y':
            exit(0)
        else:
            y.window().send_keystrokes('q')
            y.window().send_chars('q')
        time.sleep(0.7)