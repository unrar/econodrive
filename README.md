# EconoDrive 🤑

This script helps you make more money, provided a CSV file (actually, we/Numbers use `;` as a delimiter) with three columns: listing name, listing location and distance needed to travel. 

That provided, EconoDrive will tell you how to pair (and, in future releases, more travels) your drives to get a minimal driven distance.

## Usage

Place the CSV file `airbnb.csv` on the root directory. To show the help, run:

    $ python econodrive.py -h

To make the calculation not taking in account some of the listings (i.e, you've already been there), list them all:

    $ python econodrive.py -l

And take note of the IDs of the listings you want to ignore. Then run EconoDrive with the `-i` flag:

    $ python econodrive.py -i 1 2 3

This will ignore the listings with ID #1, #2 and #3. If you don't want to ignore any listings, just run it without arguments!

    $ python econodrive.py