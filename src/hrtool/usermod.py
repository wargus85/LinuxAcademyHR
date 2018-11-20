import grp, pwd, crypt, spwd, sys, subprocess, os

def add_user(name):
    #
    # If adding a user returns an error (ie, the user exists)
    # Then try updating the user instead (call mod_user)
    pass
    
def del_user(name,delete=False):
    # deleting a user should be straight forward, it will give an error if the user doesn't exist, which we can
    # ignore and continue.
    if delete == True:
        print(f"Removing user: {name}")
        try:
            with open(os.devnull, 'w') as devnull:
                deleteduser = subprocess.run(["userdel", "-r", name], check=True, stdout=devnull,stderr=devnull)

        except subprocess.CalledProcessError as err:
            if err.returncode == 1:
                print(f"You do not have permission, please check you are sudo!")
                
            elif err.returncode == 6:
                print(f"User {name} does not exist!")
                
    

def mod_user(name):
    pass
