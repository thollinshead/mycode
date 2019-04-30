#!/usr/bin/env python 3

import shutil

import os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj?')

# This line renames a file

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


