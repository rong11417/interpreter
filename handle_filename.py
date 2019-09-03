#!/usr/bin/python


import sys,subprocess,commands
#get name of file.
filename_suffix=sys.argv[1]
filename=filename_suffix.split(".")[0]
filesuffix=filename_suffix.split(".")[1]
print("filename:" + filename)
print("filesuffix:" + filesuffix)
