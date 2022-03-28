#!/bin/bash
sudo rfcomm bind rfcomm0 # CHANGEME insert Bluetooth MAC of OBDII adapter
python3 CarDashboard.py
