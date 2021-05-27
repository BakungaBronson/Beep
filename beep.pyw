import psutil
import time
from win10toast_click import ToastNotifier

#Intialize toast
toasty = ToastNotifier()

#Main function
def beeper():
    #Create battery object
    battery = psutil.sensors_battery()
    #Checks if the battery percentage is 100 and the PC is still plugged in
    if(battery.percent == 100 and battery.power_plugged == True):
        #Show toast on screen
        toasty.show_toast("Unplug Your Charger: Battery Full", "To prevent battery damage, unplug the charger from your computer.", icon_path=None, duration=None, threaded=True, callback_on_click=None)

        #Go to sleep for 30 seconds
        time.sleep(30)
    else:
        #Go to sleep for 5 seconds
        time.sleep(5)

while(1):
    beeper()