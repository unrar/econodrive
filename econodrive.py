#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from lib.airbnbs import Airbnbs
from lib.csvhandler import CsvHandler

# IDs to ignore (void by default)
igs = []

# Load the CSV file
ch = CsvHandler("airbnb.csv", ["name", "place", "km"])
deals = ch.get_dict(delim=';')

ab = Airbnbs(deals)
# Handle the arguments (-h, -i)
if len(sys.argv) > 1:
  if (sys.argv[1].lower() == "-h") or (sys.argv[1].lower == "-i" and len(sys.argv) < 3):
    print("Besides running this script without arguments, you can use the -i flag, like: ")
    print(">> python econodrive.py -i 1 3")
    print("This results in running the script just like usual, but ignoring the entires with ID #1 and #3")
    print("You can also use -l, to list your entries and find out which ID they have:")
    print(">> python econodrive.py -l")
    sys.exit(0)
  elif sys.argv[1].lower() == "-l":
    ab.list_deals()
    sys.exit(0)
  elif sys.argv[1].lower() == "-i":
    # Split the arguments to get only the IDs
    splat = sys.argv[2:]
    for n in splat:
      igs.append(int(n))

# Continue
bc = ab.best_couple(igs)

print(">> Best choice: #" + str(bc[0]) + " paired with #" + str(bc[1]) + ", driving " + str(bc[2
  ]) + "km. These listings are:\n")
ab.format_deal(bc[0])
ab.format_deal(bc[1])
