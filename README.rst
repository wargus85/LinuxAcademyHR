Linux Academy Python3 for System Admins Course Final Project
============================================================

The final project:
Python package to manage users on a server based on an “inventory” JSON file.

Preparing the Development Environment
-------------------------------------
1. Ensure that ``pip`` and ``pipenv`` are installed.
2. Clone the repository ``git clone git@github.com/wargus85/LinuxAcademyHR``
3. ``cd`` into the repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv ``python3 -m pipenv shell``

Usage
-----
Pass in an inventory file eg: ``hrtool /path/to/inventory.json``
hrtool will then parse the file and make changes according to the json:
Output will look like:
::
    Adding user 'kevin'
    Added user 'kevin'
    Updating user 'lisa'
    Updated user 'lisa'
    Removing user 'alex'
    Removed user 'alex'

Alternatively, run hrtool like: ``hrtool --export path/to/inventory.json`` to export the current settings

