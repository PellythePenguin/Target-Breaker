import pyautogui as pya
import time
import keyboard


time.sleep(3)
#Brief prep period

#print(target_location)


target_images = ['target_small.png', 'target2.png']
Tregion = (472, 504, 742, 312)
#(460,265,715,530)

def getTargetLocation():
    try:
        return pya.locateCenterOnScreen(
            'target3(best).png', grayscale=False,
            region=(Tregion),
            confidence=0.21
        )
    except Exception:
        print("No target found")
        return None
         
def breakTarget(position):
     if target_location is not None:
        pya.moveTo(position)
        pya.click()
        time.sleep(0.03)


while not keyboard.is_pressed("p"):
    target_location = getTargetLocation()
    breakTarget(target_location)

#for i in range(0,3):
 #   print(pya.position())
  #  
   # time.sleep(7)

#pya.moveTo(100,100,1)

#pya.scroll(-500)