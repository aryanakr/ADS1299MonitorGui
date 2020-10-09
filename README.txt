================
 Ads1299Monitor
================

Authors
=======

By Aryan Akbarpour - https://www.aryanakr.com

About
=====

The main purpose of this program is to allow users to monitor the data capture by Ads1299 chip (by Texas Instruments) connect to and ESP32 microcontroller. Also, this program allows to change the onboard registers on demand and record the data in csv and xlsx formats.

Usage
=====

Simply run 'python run.py' from within the project folder.

- Initialize TCP network and connect to the microcontroller by going to Options->Connect….
- Enter TCP ip and port and click on the connect button. Wait until the connection is stablished.
- You can start by creating a new register profile by going to Options->Create Register Profile.
- On the main window, select your newly created profile and click on Submit button.
- Choose the channels that you would like to monitor on Monitor->Monitor Settings
- Start the monitor by going to Monitor->Monitor.
- For recording data, start by creating a new record profile in Record->Create Data Capture Profile.
- Then open your data profile in Record->Record Data and start recording data.

Contributing
============

Submit bugs to aryan.akr@yahoo.com

Notes
=====

This program is accompanied by an Arduino project for ESP32 microcontroller