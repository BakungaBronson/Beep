import psutil
import time
#from plyer import notification
from win10toast_click import ToastNotifier

class BatteryNotifier:

    #Constructor function
    def __init__(self):
        # initialize 
        toaster = ToastNotifier()
        toaster.show_toast(
            "Beep", # title
            "Beep is running in the background", # message 
            icon_path='./icon.ico', # 'icon_path' 
            duration=10, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=False, # True = run other code in parallel; False = code execution will wait till notification disappears 
            callback_on_click=None # click notification to run function 
        )

    #Main function
    def beeper(self):
        #Create battery object
        battery = psutil.sensors_battery()
        #Checks if the battery percentage is 100 and the PC is still plugged in
        if(battery.percent == 100 and battery.power_plugged == True):
            #Show toast on screen
            toaster = ToastNotifier()
            toaster.show_toast(
                "Unplug Your Charger: Battery Full", # title
                "To prevent battery damage, unplug the charger from your computer.", # message 
                icon_path='./icon.ico', # 'icon_path' 
                duration=10, # for how many seconds toast should be visible; None = leave notification in Notification Center
                threaded=False, # True = run other code in parallel; False = code execution will wait till notification disappears 
                callback_on_click=None # click notification to run function 
            )
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
