import json, sys, pwd, subprocess, spwd


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
    for user in pwd.getpwall():
        if user.pw_uid > 999:
            password = spwd.getspnam(user.pw_name).sp_pwdp
            getgroups = subprocess.run(['groups',user.pw_name],stdout=subprocess.PIPE)
            groupslist= str(getgroups.stdout).split(':')[1].split('\\')[0].strip().split(' ')
            user_dict = {
                "name":user.pw_name,
                "groups":groupslist,
                "password":password,
                "delete":"False"
                }
            with open(filename, 'a+') as f:
                f.writelines("%s\n" % str(user_dict))

            
