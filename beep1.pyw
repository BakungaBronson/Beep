import psutil
import time
import plyer.platforms.win.notification
from plyer import notification

class BatteryNotifier:

    #Constructor function
    def __init__(self):
        notification.notify("Beep has Started", "The program is running in the background.")

    #Main function
    def beeper(self):
        #Create battery object
        battery = psutil.sensors_battery()
        #Checks if the battery percentage is 100 and the PC is still plugged in
        if(battery.percent == 100 and battery.power_plugged == True):
            #Show toast on screen
            notification.notify("Unplug Your Charger: Battery Full", "To prevent battery damage, unplug the charger from your computer.")
            #Go to sleep for 30 seconds
            time.sleep(30)
        else:
            #Go to sleep for 5 seconds
            time.sleep(5)

#Creating an onject of the  BatteryNotifier object
obj = BatteryNotifier()
while(1):
    #Calling the beeper function which is responsible for the notification
    obj.beeper()