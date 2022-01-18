#!/usr/bin/python3
# Run command passed as first argument


import sys
import subprocess
import shlex

command = sys.argv

del command[0]


print (command)
subprocess.call(command)









