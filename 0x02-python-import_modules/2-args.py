#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

  if len(argv[1:]) == 0:
   print("0 arguments.")

  elif len(argv) == 2:
    print("{:d} argument:".format(len(argv[1:])))

  else:
      print("{:d} arguments:".format(len(argv[1:])))

  for x in (argv[1:]):
    print("{:d}: {}".format(argv.index(x), x))
