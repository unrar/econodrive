#!/usr/bin/python
# -*- coding: utf-8 -*-

class Airbnbs:
  """This class manages the main behavior of this application"""

  def __init__(self, dix):
    """Start an instance of the class.
      @param dix List[Dictionary]  Should be the data parsed by CsvHandler"""
    self.dix = dix

  def best_couple(self, igs=[], fix=0):
    """ Finds the best couple of entries, whose sum of the km column is the lowest """
    sums = []  # Hold sums and ID
    for firste in self.dix:
      kms = firste["km"]
      tid = firste["id"]
      # If we have fixed one of the IDs, let it be this one
      if fix:
        if not tid == fix:
          continue  # Until we get the entry we want
          
      # If we are ignoring any IDs, skip this loop
      if tid in igs:
        continue
      started = False
      lowest = 1.0
      lwid = 0
      for second in self.dix:
        # Skip if it's the same, or we're ignoring it
        if (tid != second["id"]) and (not second["id"] in igs):
          summ = kms + second["km"]
          if (started == False) or (summ < lowest):
            lowest = summ
            lwid = second["id"]

          started = True

      # Second loop finalized
      sums.append({"tid": tid, "lwid": lwid, "lowest": lowest})
      # Uncomment for debug:
      #print(">> Found a lowest match: #" + str(tid) + " + #" + str(lwid) + " = " + str(lowest) + "km.")

    # At this point we need to find out the lowest of all
    lows = []
    for dx in sums:
      lows.append(dx["lowest"])
    # Now we've found it, we need to get the ID's and return that
    abs_lowest = min(lows)
    # Uncomment for debug:
    #print str(abs_lowest)
    for dx in sums:
      if dx["lowest"] == abs_lowest:
        return [dx["tid"], dx["lwid"], dx["lowest"]]

  def format_deal(self, id): 
    for deal in self.dix:
      if deal["id"] == id:
        print(deal["name"] + " (ID #" + str(deal["id"]) + "), at " + deal["place"] + " --> " + str(deal["km"]) + "km.")

  def list_deals(self):
    """ List the entries of the provided data. """
    for deal in self.dix:
      print(deal["name"] + " (ID #" + str(deal["id"]) + "), at " + deal["place"] + " --> " + str(deal["km"]) + "km.")

