#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon
import os,sys

#Device Configs
conservationModeFile = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
installPath = os.getcwd()+"/"

iconPathOn = installPath+"iconOn.png"
iconPathOff = installPath+"iconOff.png"

#Language
activatedStr="actived"
deactivatedStr="de-activated"
conservationModeStr="Conservation mode is "

#Global variables 
option1 = QAction("ON")
option2 = QAction("OFF")
title = QAction("Conservation Mode")

conservationMode = '1' # 1 or 0

def changeState(x):
    function="echo "+str(x)+"| tee "+conservationModeFile
    os.system(function)
    newState = getOnOrOff()
    updateMenu(newState)


def updateMenu(conservationMode):
    if(conservationMode=='1') :
        option1.setEnabled(False)
        option2.setEnabled(True)
        title.setIcon(QIcon(iconPathOn))
    else:
        option1.setEnabled(True)
        option2.setEnabled(False)
        title.setIcon(QIcon(iconPathOff))

def getOnOrOff():
    return open(conservationModeFile).read()[0]


def main():
    
    #Check state on launch
    conservationMode=getOnOrOff()

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


    updateMenu(conservationMode)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()