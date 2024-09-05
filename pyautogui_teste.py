import pyautogui
import time

pyautogui.alert("Vai comecar")
pyautogui.PAUSE = 0.5
#
"""
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/u/0/folders/1aWwYk2b_AY5E-2TjZ1D8tjQIthXFSYwb")
pyautogui.press('enter')
#
"""

pyautogui.hotkey('winleft', 'r')
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.write('wmic')
pyautogui.press('enter')
pyautogui.write(r'/output:C:\users\suporte\documents\teste\ListaProgramas.txt product get name, version, installDate')
pyautogui.press('enter')

pyautogui.hotkey('winleft','e')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.write(r"C:\Users\suporte\Documents\teste")
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

pyautogui.hotkey('winleft','e')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.typewrite(r"\\192.168.2.16\Programas")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')




