#Import all necessary functions
import argparse as ap
import os
import csv
#Set up all necessary parser options
os.chdir(os.getcwd())
parser = ap.ArgumentParser(prog="ListDirectory",add_help=True,description="This program lists the contents of a directory",epilog="Ensure you enter a valid directory",usage="./12q.py [-h]")
#Set up main parser option
parser.add_argument('directory', help="Enter a directory to display contents")
#User enters -l to set the name for the log file
parser.add_argument('-l','--logfile',required=False,
help="Send output to the log file with the specified name")
#catches any exceptions
try:
    args = parser.parse_args()
except:
    print("This program is ending because of an invalid option")
    exit(1)
# prints the contents of a directory
def printDir(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
    else:
        dir_list = os.listdir(directory)
        for item in dir_list:
            print(item)

# puts the contents of a directory into a log file
def logFile(filename, directory):
    if not os.path.exists(directory):
        file = filename + ".txt"
        if os.path.exists(file):
            print("File already exists!")
            exit(1)
        with open(file, "w") as fn:
            fn.write("Directory does not exist!")
    else:
        dir_list = os.listdir(directory)
        file = filename + ".txt"
        if os.path.exists(file):
            print("File already exists!")
            exit(1)
        with open(file, "w") as fn:
            for fileName in dir_list:
                fn.write(fileName + "\n")
            fn.close()
# calls either the logfile function or the print directory function.
if args.logfile:
    logFile(args.logfile, args.directory)
else:
    print(args.directory)
    print("*************************")
    printDir(args.directory)

