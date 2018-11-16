import grp, pwd, crypt, spwd, sys, subprocess

def add_user(name):
    #
    # If adding a user returns an error (ie, the user exists)
    # Then try updating the user instead (call mod_user)
    pass
    
def del_user(name):
    # deleting a user should be straight forward, it will give an error if the user doesn't exist, which we can
    # ignore and continue.
    pass

def mod_user(name):
    pass