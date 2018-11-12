from setuptools import setup, find_packages
with open('README.rst',encoding='UTF-8') as r:
    readme = r.read()
setup(
name='hrtool',
version='0.1.0',
description='HR Tool for Linux Academy Project',
long_description = readme,
author = 'Warren',
author_email = 'warren.argus@curtin.edu.au',
install_requires=[], #This is where the required dependencies go
packages=find_packages('src'),
package_dir={'':'src'}, #this is a legacy thing that we do because of the above line
entry_points={
    'console-scripts':[
        'hrtool=hr.cli.main'
    ]
}
)