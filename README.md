# Conservation Mode Linux for Lenovo laptops

An app that helps knowing and turning on/off the conservation mode for lenovo laptops running linux.

## Works for :
Lenovo Legion 5

# Installation

1. Clone the project to a folder.

2. Go threw the .py and .sh to make sure all the folder point to the good directories.

3. Add CCM.sh to the visudo

    1. sudo visudo
    2. add : thisUser ALL=(ALL:ALL) NOPASSWD:/home/thisUser/Documents/Linux-Conservation-Mode-For-Lenovo/CCM.sh 

4. Optional : Add to startup applications

