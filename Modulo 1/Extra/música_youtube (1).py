import pyautogui as pag
from time import sleep


pag.mouseInfo()
 
pag.press('win')
pag.write('chrome')
pag.press('enter')
pag.moveTo(343,61)
sleep(2)
pag.click()
sleep(2)
pag.write('www.youtube.com.br')
pag.press('enter')
sleep(2)
pag.moveTo(742,111)
pag.click()
pag.write('The hils -The weeknd')
pag.press('enter')
pag.moveTo(697,336,duration=1)
pag.click()
