from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, operator
from collections import defaultdict
from builtins import *
from pprint import pprint

server = "http://rest.ensembl.org"

class Tissue:
  def __init__(self, tissue, rec):
    self.tissue           = tissue
    self.rec              = rec
    self.hits             = []
    self.sig_hits         = []
    self.sig_hits_sorted  = []

    # Load data into array, created subset with significant hits
    for hit in self.rec:
      self.hits.append((hit['value'], hit['gene']))
      if hit['value'] < 0.005:
        self.sig_hits.append((hit['value'],hit['gene']))
    
    # Best hits first
    self.sig_hits_sorted = (sorted(self.sig_hits, key=lambda sig_hits_sorted: sig_hits_sorted) )


def get_descriptions (ensid):
  ext='/xrefs/id/%s' %(ensid)
  decoded = request(ext)
  for xref in decoded:
    if (xref['description']) and (xref['dbname']):
      print("DB: %s\tDescription: %s" %(xref['dbname'], xref['description'] ))


# Used for resolving requests and decode the JSON
def request (ext):
  r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
  if not r.ok:
    r.raise_for_status()
    sys.exit()
  decoded = r.json()
  return decoded;


## List Returns all tissues currently available in Homo sapiens
ext='/eqtl/tissue/homo_sapiens'
decoded = request(ext)
#print json.dumps(decoded, indent=4, sort_keys=True)

# Examine a variant  
variant = 'rs2736340'
# Generic information
ext='/variation/human/%s' %(variant)
decoded = request(ext)
print(json.dumps(decoded, indent=4, sort_keys=True))



# Look for the SNP in a specific specific tissue
tissue='Whole_Blood'
ext='/eqtl/variant_name/homo_sapiens/%s?statistic=p-value;tissue=%s;' %(variant, tissue)
decoded = request(ext)
#print(json.dumps(decoded, indent=4, sort_keys=True))

t = Tissue(tissue, decoded)
for k, v in t.sig_hits_sorted:
  print("Gene: %s\tp-value: %s" %(v, k) )
  get_descriptions(v)
  print()
#  print(json.dumps(decoded, indent=4, sort_keys=True))

  


