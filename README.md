# Linux Conservation Mode for Lenovo laptops

A tray application that shows the status of conservation mode and helps you enable it or disable it!

<p align="center">
  <img src="https://github.com/liperium/Linux-Conservation-Mode-For-Lenovo/blob/main/demo.gif" alt="Demo of the tray service"/>
</p>

## Works for :

- Lenovo Legion 5

Many more laptops can be adapted with the right settings in the .py and .sh

# Installation

1. Clone the project to a folder. (Mine is in ~/Documents)

2. Go threw the .py and .sh to make sure all the folder point to the good directories.

3. Add CCM.sh to the visudo

    1. sudo visudo
    2. Add to the end : 
    
            thisUser ALL=(ALL:ALL) NOPASSWD:/home/thisUser/Documents/Linux-Conservation-Mode-For-Lenovo/CCM.sh 

4. Optional : Add to startup applications

### Make sure your python env is setup correcly as this is a python app
https://stackoverflow.com/questions/3655306/ubuntu-usr-bin-env-python-no-such-file-or-directory
