import os
import csv
#import sys
#from datetime import datetime

cwd = os.getcwd()
# Set path for files
print(cwd)
files = os.listdir(cwd)
for f in files:
	print(os.path.join(cwd, f))