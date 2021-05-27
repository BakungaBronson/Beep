### Beep V1.0

## Operating System
This program runs on Windows 10 so far. The next version will support Linux and Mac Os.

## Description
After having a number of laptops over the years. I have come to realise that the number one cause of battery damage for the average laptop user is overcharging. This can happen when we become too busy to keep track of the battery percentage down in the taskbar and as a result, we leave the battery plugged in for anything from 10 more minutes all the way up to 3 hours before noticing that the battery is full.

Beep is a python3 program that uses toast notifications to inform the user when their battery is full in an attempt to stop laptop battery damage due to overcharging. 

## Requirements
This python program uses two libraries namely: psutil and win10toast_click. Both can be installed using pip with the "pip install psutil" and "pip install win10toast_click" commands respectively. If you however use the windows executable there is no need to install the above dependencies because they are bundled into the executable found in the dist folder.

## In Progress
An installer will be available on the next commit so as to make it easy to install and run the app on startup. For now the program can be run by placing a shortcut of the beep1.exe program in the StartUp Folder which can be accessed by using the Run utility.

# Instructions to include startup shortcut in the startup folder
1. In the search bar on th taskbar, type in "run" and execute the application.
2. Type "shell:startup" in the Run program
3. Copy the "beep1.exe"
4. Right click and select "Paste shortcut" in Startup folder we opened earlier using run.