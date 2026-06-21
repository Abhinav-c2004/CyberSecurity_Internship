# system_information.py

import os
import platform
import sys

print("===== SYSTEM INFORMATION =====")
print("Operating System Name :", platform.system())
print("Current Username      :", os.getlogin())
print("Current Working Directory :", os.getcwd())
print("Python Version        :", sys.version)