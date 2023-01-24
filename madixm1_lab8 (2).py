#Matt Madix
#Import all necessary functions
import argparse as ap
import os
import csv
import re
import shutil
os.chdir(os.getcwd())
#Set up all necessary parser options
def get_parser():
    parser = ap.ArgumentParser(prog="lab8", usage="USAGE:<script name> [-h|-p|-c FileName|-a fileName]", add_help=True)
    #sets main command as filename
    parser.add_argument('filename', help="Enter the file name you wish to view")
    #user enters -p to call print_incorrect_users function
    parser.add_argument("-p", "--pwd", action="store", help="List all password not up to company standards")
    #user enters -c to call get_compromised_computers function
    parser.add_argument("-c", "--comp", action="store", help="Check for compromised passwords")
    #user enters -a to call rename_department function
    parser.add_argument("-a", "--accdept", action="store", help="Change Accounting department to Finance department")
    return parser

#Prints the list of compromised computers to a file
def get_compromised_computers(file, newfile):
    cCregex = r'200.10.15.()'
    with open(file, 'r') as filer:
        csv_reader = csv.reader(filer, delimiter=',')
        next(csv_reader)
        for lines in csv_reader:
            ip = str(lines[3])
            if re.match(cCregex, ip, re.IGNORECASE) is not None:
                with open(newfile, "w") as comp:
                    comp.write(lines[0] + " " + lines[1]+ ", " + lines[4] + ", " + lines[2] + "\n")
#prints the list of incorrect passwords to the command line
def print_incorrect_users(file):
    with open(file, 'r') as filer:
        csv_reader = csv.reader(filer, delimiter=',')
        next(csv_reader)
        for lines in csv_reader:
            password = str(lines[6])
            if len(password) < 10 or len(password) > 15:
                print(lines[0] + " " + lines[1])
            elif not bool(re.search(r'[A-Z]', password)):
                print(lines[0] + " " + lines[1])
            elif not bool(re.search(r'[a-z]', password)):
                print(lines[0] + " " + lines[1])
            elif not bool(re.search(r'\d',password)):
                print(lines[0] + " " + lines[1])
            elif not bool(re.search(r'[#@!]',password)):
                print(lines[0] + " " + lines[1])
#prints the names of all members of the accounting department and creates a new list of users with Accounting changed to Finance
def rename_department(file, newfile):
    in_file = open(file, "rt")
    reader = csv.reader(in_file)
    out_file = open(newfile, "wt")
    writer = csv.writer(out_file)
    for row in reader:
        newrow = [re.sub(r"Accounting", "Finance", item) for item in row]
        writer.writerow(newrow)
    with open(file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for lines in csv_reader:
            dept = str(lines[4])
            if bool(re.search(r'^Accounting$', dept)):
                print(str(lines[0]) + " " + str(lines[1]))
#main function calls all other functions
def main():
    psr = get_parser()
    # catches any exceptions
    try:
        args = psr.parse_args()
    except Exception as ex:
        print("Error")
    else:
        if args.comp:
            if os.path.exists(args.comp):
                print("File already exists!")
                exit(1)
            else:
                get_compromised_computers(args.filename, args.comp)
        if args.pwd:
            print_incorrect_users(args.filename)
        if args.accdept:
            if os.path.exists(args.accdept):
                print("File already exists!")
                exit(1)
            else:
                print("Finance Department Memebrs:")
                rename_department(args.filename, args.accdept)
#runs main function
main()