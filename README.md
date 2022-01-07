# Linux Conservation Mode for Lenovo laptops

A tray application that shows the status of conservation mode and helps you enable it or disable it!

<p align="center">
  <img src="https://github.com/liperium/Linux-Conservation-Mode-For-Lenovo/blob/main/demo.gif" alt="Demo of the tray service"/>
</p>

## Works for :

- Lenovo Legion 5

Many more laptops can be adapted with the right settings in the .py and .sh

# Installation

## If you have the same laptop ( code : VPC2004:00 )
1. Download from release

2. Remove sudo permissions to edit conservation_mode value

       sudo chmod +666 /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

3. Optional : Add to startup applications, add as .desktop

## If you have another laptop 
1. Download source code

2. Edit the vars to fit for your laptop

3. Compile with auto-py-to-exe or run direcly with python ( don't forget to put icons in the same folder )

4. Optional : Add to startup applications, add as .desktop

### Make sure your python env is setup correcly as this is a python app
https://stackoverflow.com/questions/3655306/ubuntu-usr-bin-env-python-no-such-file-or-directory
