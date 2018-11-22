import grp, pwd, crypt, spwd, sys, subprocess, os



def add_user(name,groups,password):
    #
    # If adding a user returns an error (ie, the user exists)
    # Then try updating the user instead (call mod_user)
    #need to check that the groups exist
    for group in groups[0].split(','):
        try:
            exists = grp.getgrnam(group)
        except KeyError as Err:
            #the group does not exist so add it in
            addgroup = subprocess.run(['adduser',group])
            print(f"Creating group: f{group}")
    
    print(f"Adding: {name}")
    try:
        user = pwd.getpwnam(name)
    except KeyError as err:
        # User does not exist, so we can go ahead and add
        with open(os.devnull, 'w') as devnull:
            adduser = subprocess.run(
                ['useradd', '-m', '-s', '/bin/bash', '-p', password, '-G', groups[0], name], check=True)
            print(f"Added user {name}")

    
def del_user(name,delete=False):
    # deleting a user should be straight forward, it will give an error if the user doesn't exist, which we can
    # ignore and continue.
    if delete == True:
        print(f"Removing user: {name}")
        try:
            with open(os.devnull, 'w') as devnull:
                deleteduser = subprocess.run(["userdel", "-r", name], check=True, stdout=devnull,stderr=devnull)
                print(f"Deleted user {name}")

        except subprocess.CalledProcessError as err:
            if err.returncode == 1:
                print(f"You do not have permission, please check you are sudo!")
                
            elif err.returncode == 6:
                print(f"User {name} does not exist!")
                
    

def mod_user(name,groups,password):
    # Check that the user exists, if not, then create the user with a call
    # to add_user()


    # Check that all the groups exist:
    for group in groups[0].split(','):
        try:
            exists = grp.getgrnam(group)
        except KeyError as Err:
            #the group does not exist so add it in
            addgroup = subprocess.run(['adduser',group])
            print(f"Creating group: f{group}")

    #Modify the user now that all the groups exist.

    
