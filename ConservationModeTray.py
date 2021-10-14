from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon
import os,sys

device="VPC2004:00"
file = "/sys/bus/platform/drivers/ideapad_acpi/"+device+"/conservation_mode" # /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
iconPath = "/home/liperium/Documents/ConservationMode/output/icon.png"
activatedStr="actived"
deactivatedStr="de-activated"
conservationModeStr="Conservation mode is "

option1 = QAction("ON")
option2 = QAction("OFF")

def changeState(x):
    function="sudo /home/liperium/Documents/ConservationMode/output/script.sh "+str(x)#+" "+file
    os.system(function)
    updateMenu()
    #script.sh = echo "$1"| sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

def updateMenu():
    s=open(file).read()

    if(s=="1" or s=="1\n") :
        option1.setEnabled(False)
        option2.setEnabled(True)
    else:
        option1.setEnabled(True)
        option2.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    trayIcon=QSystemTrayIcon(QIcon(iconPath))
    trayIcon.setVisible(True)

    menu = QMenu()
    title = QAction("Conservation Mode")
    title.setIcon(QIcon(iconPath))
    title.setEnabled(False)
    menu.addAction(title)

    menu.addSeparator()

    option1.triggered.connect(lambda:changeState(1))
    option2.triggered.connect(lambda:changeState(0))
    menu.addAction(option1)
    menu.addAction(option2)

    menu.addSeparator()

    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    trayIcon.setContextMenu(menu)

    updateMenu()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()