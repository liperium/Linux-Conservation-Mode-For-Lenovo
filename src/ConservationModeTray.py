#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon
import os,sys

conservationModeFile = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

#Language
activatedStr="actived"
deactivatedStr="de-activated"
conservationModeStr="Conservation mode is "

#Global variables
option1 = QAction("ON")
option2 = QAction("OFF")
title = QAction("Conservation Mode")

conservationMode = 1

def getOnOrOff():
    return open(conservationModeFile).read()[0]

def changeState(x):
    function="sudo "+os.path.join(installPath,"CCM.sh")+" "+str(x)
    os.system(function)
    
    updateMenu()


def updateMenu():
    if(getOnOrOff()=='1') :
        option1.setEnabled(False)
        option2.setEnabled(True)
        title.setIcon(QIcon(iconPathOn))
    else:
        option1.setEnabled(True)
        option2.setEnabled(False)
        title.setIcon(QIcon(iconPathOff))

def main():

    global installPath
    installPath = os.getcwd()

    global iconPathOn 
    iconPathOn = os.path.join(installPath,"iconOn.png")
    global iconPathOff 
    iconPathOff = os.path.join(installPath,"iconOff.png")

    app = QApplication(sys.argv)
    menu = QMenu()

    defaultIcon = QIcon(iconPathOn)

    app.setQuitOnLastWindowClosed(False)
    sysTray=QSystemTrayIcon(defaultIcon)
    sysTray.setVisible(True)

    #Conservation Mode
    
    title.setIcon(defaultIcon)
    title.setEnabled(False)
    menu.addAction(title)

    #-----
    menu.addSeparator() 

    #ON
    option1.triggered.connect(lambda:changeState(1))
    menu.addAction(option1)
    #OFF
    option2.triggered.connect(lambda:changeState(0))
    menu.addAction(option2)

    #-----
    menu.addSeparator() 

    #Quit
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    sysTray.setContextMenu(menu)


    updateMenu()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()