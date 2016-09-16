# Author: federica bianco, NYU, September 2016
##############################
# Code written to demonstrate ho to pass arguments to a python script
# for HW2 of PUI2016
# http://cosmo.nyu.edu/~fb55/PUI2016
##############################
# put the name of the outut file as input argument:
# i.e. run the code as
#      python aPythonScriptThatWritesToCSV.py mycvs.csv
###########

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function
# the next import allows me to read line input arguments
import sys


# this line checks how many arguments are passed to python
# the arguments are stored in sys.argv which is a list
# the first argument is the name of the code
# so sys.argv is a list with at least one element
# with the output filename in input it will be a list of 2
# if you add more than one word as argument it will give you an error as well
if not len(sys.argv) == 2:
    print("Invalid number of arguments. Run as: python aPythonScriptThatWritesToCSV.py mycvs.csv")
    sys.exit()

# this line opens a file for writing using the name you chose
# the "w" tells it you are opening for writing, not reading
fout = open(sys.argv[1], "w")

# this line prints the numbers from 1 to 10 separated by commas
# 10 times in 10 rows
# to your output file
# notice the "\n" character at the end of each line:
# that's the line break
for i in range(10):
    fout.write("1,2,3,4,5,6,7,8,9,10\n")

# that's a way to write to a csv file!
