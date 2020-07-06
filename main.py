import pyautogui as bot

import time as t

def moveDown(x):

    i = 0

    for i in range(x):

        bot.press('down')

        i += 1


t.sleep(1)

bot.hotkey('ctrl', 'alt', 't')

t.sleep(3)

bot.write('firefox')

bot.press('enter')

t.sleep(2)

bot.write('intagram.com')

bot.press('enter')

t.sleep(15)

emailfieldlocation = bot.locateOnScreen('inputemail.png')

t.sleep(1)

print(emailfieldlocation)

emailfield = bot.center(emailfieldlocation)

t.sleep(1)

print(emailfield)

bot.click(emailfield)

bot.write('your_username_or_email')

bot.press('tab')

bot.write('your_password')

bot.press('enter')

# log in finished

t.sleep(5)

# save login page

notnowlocation = bot.locateOnScreen('notnow.png')

print(notnowlocation)

notnowbtn = bot.center(notnowlocation)

bot.click(notnowbtn)

t.sleep(2)

# let's loop the like

while True:

    bot.doubleClick(520, 600)

    moveDown(20)
