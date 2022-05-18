#!/usr/bin/env python3
"""A script to move two files into a directory"""


# standard library imports
import shutil   # shell utilities will be used to move files
import os       # provies access to low level os operations 

def main():
    """called at runtime"""
    
    #move into given working dir
    os.chdir('/home/student/mycode/day3/')
    
    #move raynore into ceph
    shutil.move('raynor.obj', 'ceph_storage/')

    # program will pause while we accept input from user
    xname = input('What is the new name for kerrigan.obj? ')

    #move kerrigan into ceph with a new name from input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main() # this calls our main function
