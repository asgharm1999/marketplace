"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

import pip

def import_or_install(package):
    try:
        __import__(package)
    except:
        pip.main(['install', package])