#!/usr/bin/python

import os
import glob
from os import system
from shutil import copyfile
import re
import string
import sys

system('clear') # Clear the screen and start fresh
rs=system('make makestr.x')  # need the exit status here...
if rs!=0: sys.exit("\n\nCompilation of makestr.x failed\n")

#tests=glob.glob('tests/struct_enum.in.*')
#f=open('tests/list')

system('rm vasp.0007')
system('./makestr.x ./tests/13struct.out 7')
rs=system('diff -q vasp.0007 tests/vasp.0007_from2x3_Rods_case')
if rs!=0:
    sys.exit("\n --- Failure in the first of Rod's 2x3 cases ---\n")
else:
    print "\n <<< First test of makestr.x passed >>>\n"

#for itest in tests:
#    # Define a regexp for catching the test #
#    r1 = re.compile('.*struct_enum\.in\.(...)') 
#    m = r1.match(itest) # Make the match
#    Nt = m.group(1)     # Pull out the group from the match --- the Test Number
#    print "Starting Test "+Nt+"..."
#    print string.rstrip(f.readline()) # Print corresponding line from "testlist"
#
#    copyfile('tests/struct_enum.in.'+Nt,'struct_enum.in')
#    system('./multienum.x')
#    # Check for difference between this run and saved output 
#    rs=system('diff -q  struct_enum.out tests/struct_enum.out.'+Nt)
#    
#    if rs!=0:
#	#system('diff struct_enum.out tests/struct_enum.out.'+Nt)
#	#raw_input()
#	sys.exit("\n\nFailure in Test #:"+Nt)
#	#copyfile('test.out','tests/'+Nt+'.out')
#	print "\n\nFailure in Test #:"+Nt
#    else: print "Test",Nt,"Passed"
#    #system('rm str?.txt')
    #system('rm test.out '+Nt+'.out')

#print "\n <<< All tests passed >>>\n"
