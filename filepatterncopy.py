#!/usr/bin/python

"""
@version: 1.0
@author: Krishnan
@summary: This python script will search files of given pattern from src dir and copy it to given destination path
"""

"""
import the necessary libraries
"""
import sys
import glob
import shutil
import argparse

""" util methods:"""

def patternsrchcopy(srcdir, dstdir, pattern='*'):
    src_dir=srcdir
    dest_dir=dstdir
    pattern=pattern
    listfiles=glob.iglob(src_dir+'/'+pattern)
    #iterate the files in listfiles
    for f in listfiles:
        shutil.copy(f, dest_dir)

"""main program starts from here:"""            


try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--src", help="provide the src folder path")
    parser.add_argument("-d","--dst", help="provide the destination folder path")
    parser.add_argument("-p","--pattern", help="pattern to be searched needs to be provided")
    args=parser.parse_args()
        
    if args.src:
        srcdir = args.src
    else:
        raise Exception
    
    if args.dst:
        dstdir = args.dst
    else:
        raise Exception
    
    if args.pattern:
        pattern = args.pattern
    else:
        raise Exception  
            
    #call the pattern search method:
    patternsrchcopy(srcdir,dstdir,pattern)    
except Exception as msg:
    print(msg)
    
sys.exit(0)
