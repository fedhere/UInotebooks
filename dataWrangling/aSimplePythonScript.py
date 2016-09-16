# Author: federica bianco, NYU, September 2016
##############################
# Code written to demonstrate ho to pass arguments to a python script
# for HW2 of PUI2016
# http://cosmo.nyu.edu/~fb55/PUI2016
##############################
# put your name as input argument:
# i.e. run the code as
#      python aSimplePythonScript.py Dr.Bianco
# notice that your name should be a single word (only the first line argument is read)

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
# with your name in input it will be a list of 2
# if you add more than one word as argument it will give you an error as well
if not len(sys.argv) == 2:
    print("Invalid number of arguments. Run as: python  aSimplePythonScript.py YourNameHere")
    sys.exit()

# this line prints Hallo and then your name
# which you provide as argument
print("Hallo " + sys.argv[1] + "!")
