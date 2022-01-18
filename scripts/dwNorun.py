#!/usr/bin/python3
# dummy script to not Run command passed as first argument


import sys
import subprocess
import shlex

command = sys.argv

del command[0]


print (command," not run")










