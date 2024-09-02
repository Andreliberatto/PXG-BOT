import pyautogui
import random
from time import sleep
import myKeyboard
import keyboard
import reapet_atack

FISHING_POSITION =(915,87),(383,162),(1144,87),(1143,391),(1296,315)
IMG_BUBBLE_SIZE= (75,93)
MINIGAME = (947,343,31,396)
attack = ("f6,f6,f8")

def set_fishing_rod():
    area = random.choice(FISHING_POSITION)
    center_area = pyautogui.center(area+IMG_BUBBLE_SIZE)
    pyautogui.moveTo(center_area)
    sleep(0.5)
    myKeyboard.press("caps")
    return area

def wait_bubble(fishing_position):
    while True:
        bubble = pyautogui.locateOnScreen("bubble.png",confidence=0.8, region=fishing_position+IMG_BUBBLE_SIZE)
        if bubble != None:
            myKeyboard.press("caps")
            break
def minigame():
    sleep(1)
    peixe = True
    while peixe != None:
        peixe = pyautogui.locateOnScreen('fish.jpg',confidence=0.8, region=MINIGAME,grayscale=True)
        barra = pyautogui.locateOnScreen('barra.jpg',confidence=0.8, region=MINIGAME)
        if peixe != None and barra != None:
            if barra.top > peixe.top:
                myKeyboard.key_down(0x39)
        else:
            myKeyboard.release_key(0x39)
    else:
        myKeyboard.key_down
        myKeyboard.release_key

def attack():
    my_attacks = ("f6,f7,f8")
    for attack in my_attacks:
        myKeyboard.press(attack)

keyboard.wait("h")

while True:
    print("iniciando pesca")
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    minigame()
    sleep(5)
    myKeyboard.press("f12")
    reapet_atack("F1...")