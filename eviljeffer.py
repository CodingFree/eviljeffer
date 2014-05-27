#!/usr/bin/python

import sys, getopt, os
import zipfile

def printhelp():
  print 'eviljeffer.py -i <inputfile> -o <outputpath>'

def main(argv):
   inputfile = ''
   outpath = ''
   try:
     opts, args = getopt.getopt(argv, "i:o:")
   except getopt.GetoptError:
     printhelp()
     sys.exit(2)
   for opt, arg in opts:
     if opt == '-h':
        printhelp()
        sys.exit()
     else:
       if opt in ("-i", "--file"):
         inputfile = arg
   if not os.path.isfile(inputfile):
     print 'Input file does not exist'
     sys.exit(2)
   else:
     print 'Input file: ', inputfile
   
   if opt in ("-o", "--output"):
     outpath = arg
     if os.path.exists(outpath):
       print 'Output path: ', outpath
     else:
       print 'Not a valid ouput path'
       sys.exit(2)
   else:
     print 'Current path as output by default'
     outpath = "."
  
   if not inputfile.endswith("zip"):
     print 'It is not a zip!'
   else:
     fh = open(inputfile, 'rb')
     zip = zipfile.ZipFile(fh)
     for name in zip.namelist():
       zip.extract(name, outpath)
     fh.close()
if __name__ == "__main__":
   main(sys.argv[1:])