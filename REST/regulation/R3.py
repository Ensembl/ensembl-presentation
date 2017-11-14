from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, operator, ensembl_rest, pprint
from builtins import *
from collections import defaultdict

server = "http://rest.ensembl.org"


# Fetch descriptions for gene using the xref endpoint
def get_descriptions (ensid):
  request='/xrefs/id/%s' %(ensid)
  decoded = ensembl_rest.get_endpoint(server, request)
  desc = []
  for xref in decoded:
    if (xref['description']) and (xref['dbname']):
      string = "DB: %s\tDescription: %s" %(xref['dbname'], xref['description'] )
      desc.append(string)
  return desc

# get genomic location and most severe consequence 
# Add all traits 
def parse_variant_phenotypes(rs, var):
  r = defaultdict(list)
  r['genomic_location']       = var['mappings'][0]['location']
  r['most_severe_consequence']= var['most_severe_consequence']
  
  trait = {}
  for p in var['phenotypes']:
    trait[p['trait']] = 1;
  
  for n in trait:
    r['trait'].append(n)
  return r

"""
  Main
"""


# 1. Using the variation endpoint retrieve all information about the variant, including phenotypes, their most severe consequence and traits.  
variant = 'rs2736340'
request ='/variation/human/%s?phenotypes=1' %(variant)
decoded = ensembl_rest.get_endpoint(server, request)
result  = parse_variant_phenotypes(variant, decoded)
print(json.dumps(result, indent=4, sort_keys=True))
  
# 2. Find where the variant is located and if it overlaps any regulatory feature
request='/overlap/region/human/%s?feature=regulatory' %(result['genomic_location'])
decoded = ensembl_rest.get_endpoint(server, request)
print(json.dumps(decoded, indent=4, sort_keys=True))


# 3. List Returns all tissues currently available in Homo sapiens
request='/eqtl/tissue/homo_sapiens'
decoded = ensembl_rest.get_endpoint(server, request)
print (json.dumps(decoded, indent=4, sort_keys=True))

# 4. 
#  Rheumatoid arthritis, SYSTEMIC LUPUS ERYTHEMATOSUS are auto-immune diseaeses. Kawasaki disease is a rare childhood illness that affects the blood vessels. 
#  Choose Whole_Blood ase tissue for the next step 

# Given the phenotypes retrieved above, select the most relevant tissue.
# Find all genes associated with the genomic variant of interest (p-value <0.00005)
# List their descriptions (xref)

tissue='Whole_Blood'
request='/eqtl/variant_name/homo_sapiens/%s?statistic=p-value;tissue=%s;' %(variant, tissue)
decoded = ensembl_rest.get_endpoint(server, request)
#print(json.dumps(decoded, indent=4, sort_keys=True))

# Only keep significant hits(p-value <0.00005)
sig_hits = []
for hit in decoded:
  if hit['value'] < 0.000005:
    sig_hits.append((hit['value'],hit['gene']))

# Best hits first
sig_hits_sorted = (sorted(sig_hits, key=lambda sig_hits_sorted: sig_hits_sorted) )
 
# print everything
for pvalue, gene in sig_hits_sorted:
  print("Gene: %s\tp-value: %s" %(gene, pvalue) )
  descs = get_descriptions(gene)
  for string in descs:
    print("\t%s" %string)
  print()


  

