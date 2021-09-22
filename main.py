import PIL.ImageGrab
import keyboard
import time

t = 0.079  # Idle time for the animation


def play():
    keyboard.press_and_release('left')  # 2 free chops at the start
    time.sleep(float(t))
    keyboard.press_and_release('left')
    time.sleep(float(t))
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('p'):  # if key 'p' is pressed
                print('You Pressed A Key!')
                break  # finishing the loop
            rgb = PIL.ImageGrab.grab().load()[1008, 534]  # Grabbing single pixel of the right branch
            if rgb == (161, 116, 56):
                print('Tree on the right!')
                keyboard.press_and_release('left')
                time.sleep(float(t))
                keyboard.press_and_release('left')
                time.sleep(float(t))
            else:
                print('Tree on the left!')
                keyboard.press_and_release('right')
                time.sleep(float(t))
                keyboard.press_and_release('right')
                time.sleep(float(t))
        except:
            print('Pressed wrong button')
            break  # if user pressed a key other than the given key the loop will break

    return 0


while True:  # Waiting for space input
    try:
        if keyboard.is_pressed('space'):  # start on space pressed
            time.sleep(0.4)  # some idling
            print('starting')
            play()
            break
    except:
        break
