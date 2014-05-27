#!/usr/bin/python

import sys, getopt, os
import zipfile

def printhelp():
  print 'eviljeffer.py -i <inputfile> -o <outputpath>'

def main(argv):
   inputfile = ''
   outputpath = ''
   try:
     opts, args = getopt.getopt(argv, "i:o:")
   except getopt.GetoptError:
     printhelp()
     sys.exit(2)
   for opt, arg in opts:
     if opt == '-h':
        printhelp()
        sys.exit()
     elif opt in ("-i", "--ifile"):
        inputfile = arg
	if not os.path.isfile(inputfile):
	  print "Input file does not exist"
	  sys.exit(2)
     else:
       printhelp()
       sys.exit(2)
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
