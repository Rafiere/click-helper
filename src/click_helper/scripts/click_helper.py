import pyautogui
import time
import subprocess

print('Test')
time.sleep(1)

# subprocess.run(['google-chrome'])
time.sleep(1)
# pyautogui.
subprocess.Popen(['google-chrome'])
time.sleep(5)
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('ctrl', 'l')

pyautogui.moveTo(100)

pyautogui.write("Hello, World!")
print('Done')

# básico já foi. agora preciso cuidar de todas as outras partes.
