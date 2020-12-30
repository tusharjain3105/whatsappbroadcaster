import webbrowser
import keyboard
import time
import numbersfromvcf
    
msg = "Hello"
for number in numbersfromvcf.numbers('akash.vcf'):
    webbrowser.open(f"https://wa.me/91{number[-10:]}?text={str(msg)}")
    time.sleep(5)
    keyboard.press_and_release('alt + tab')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl + F4')
    time.sleep(0.1)
    keyboard.press_and_release('alt + tab')
    # keyboard.press_and_release('enter, enter, enter')

