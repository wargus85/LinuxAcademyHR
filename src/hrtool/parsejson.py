import json, sys, pwd, subprocess


def readfile(filename):
    try:
        with open(filename,'r') as f:
            users = json.load(f)
    except FileNotFoundError as err:
        print(f"The file does not exist, please check the file and try again")
        sys.exit(1)
    return users

def writefile(filename):
    #Get all the users with a UID over 999
    i=1000
    try:
        user=pwd.getpwuid(i)
        password = spwd.getspnam(user.pw_name).sp_pwdp
        getgroups = subprocess.run(['groups',user.pw_name],stdout=subprocess.PIPE)
        groupslist= str(getgroups.stdout).split(':')[1].split('\\')[0].strip().split(' ')
        newgroup=""
        for group in groupslist:
            newgroup=newgroup+","+"'"+group+"'"
        newgroup=newgroup.lstrip(',')
        blah = {
            "name":f"'{user.pw_name}'",
            "groups":f"[{newgroup}]",
            "password":f"'{password}'",
            "delete":"False"
            }

    with open(filename,'w') as f:
        f.writelines(f"{users}")

            