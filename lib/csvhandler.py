#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

""" This file handles CSV parsing """

class CsvHandler:

  def __init__(self, filename, fields):
    self.filename = filename
    self.fields = fields

  def get_dict(self, delim=';'):
    with open(self.filename, 'r') as f:
      reader = csv.DictReader(f, fieldnames=self.fields, delimiter=delim)
      return self.prepare(list(reader))

  def prepare(self, olist):
    """ Add an ID to every key of a list of dictionaries, and re-format numbers """
    n = 1
    for row in olist:
      row["id"] = n
      n += 1
      # Get the 'km' field and make sure it's a float with proper dot-format
      okm = row["km"]
      nkm = okm.replace(",", ".")
      row["km"] = float(nkm)
    return olist