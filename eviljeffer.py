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
      if opt in ("-o", "--path"):
        outpath = arg
  try:
    fh = open(inputfile, 'rb')
  except IOError as e:
    print e.strerror
    sys.exit(2)

  zip = zipfile.ZipFile(fh)
  try:
    for name in zip.namelist():
      zip.extract(name, outpath)
    fh.close()
  except OSError as e:
    print e.strerror
    sys.exit(2)
if __name__ == "__main__":
  main(sys.argv[1:])