import pytest
from hrtool import usermod

user = {
    'name':'kevin',
    'groups':['wheel,dev'],
    'password':'$6$hPckApj16w9iJIoF$9aWAdWEeIsWcSAoMZL94Dw.aRXe/clyl0na8i2GhnfqKjTBfAnA/DH4RtEyp9lJTQbnIeZbJjWUC140.bBCCh.',
    'delete':'True'
    }



def test_add_existing_user(mocker):
    '''
    Test to add a user that already exists will update the user instead
    '''
    mocker.patch('subprocess.run')
    
    pass

def test_add_new_user():
    '''
    Test to add a user that does not already exist 
    '''
    pass

def test_del_existing_user():
    '''
    test delete a user that exists
    '''
    pass

def test_del_non_existing_user():
    '''
    test delete a user that does not exist
    '''
    pass

def test_modify_existing_user():
    '''
    test modifying an existing user
    '''
    pass

def test_modify_non_existing_user():
    '''
    test modifying an non existant user
    '''
    pass