
import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

colorSelected = 'start'

'''
FUNCTION
'''
def userInputMenu():
    print('Enter an option based on the color you want the Circuit to display')
    print('For RED color, type 1')
    print('For GREEN color, type 2')
    print('For BLUE color, type 3')
    print('For WHITE color, type any valid integer')
    print('To quit the program, type q or Q')
    return input()
'''
ENDS
'''

colorSelected = userInputMenu()
while colorSelected != 'q' or colorSelected != 'Q':
    if (colorSelected == 'q') or (colorSelected == 'Q'):
        leddsOf = (0,0,0)
        #Turn off the leds
        for i in range(10):
            cp.pixels[i]=leddsOf
        
        break
    try:
        colorSelected = int(colorSelected) #int(input())
    except:
        print('You have entered an invalid option.')

    leddsOf = (0,0,0)
    #Turn off the leds
    for i in range(10):
        cp.pixels[i]=leddsOf

    ledsOn = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    option = (0,0,0)
    
    if (colorSelected == 1):
        ledsOn = red
    elif (colorSelected == 2):
        ledsOn = green
    elif (colorSelected == 3):
        ledsOn = blue
    
    for i in range(10):
        cp.pixels[i] = ledsOn
    cp.pixels.show()
    time.sleep(0.3)

    colorSelected = userInputMenu()

