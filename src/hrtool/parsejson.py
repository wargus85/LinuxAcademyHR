import json, sys 

def readfile(filename):
    try:
        with open(filename,'r') as f:
            users = json.load(f)
    except FileNotFoundError as err:
        print(f"The file does not exist, please check the file and try again")
        sys.exit(1)
    return users

def writefile(filename):
    pass        