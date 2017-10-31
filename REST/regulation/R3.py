from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, operator, pprint
from builtins import *
from collections import defaultdict

server = "http://rest.ensembl.org"


# Used for storing information about the tissue
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
      if hit['value'] < 0.000005:
        self.sig_hits.append((hit['value'],hit['gene']))
    
    # Best hits first
    self.sig_hits_sorted = (sorted(self.sig_hits, key=lambda sig_hits_sorted: sig_hits_sorted) )

# Fetch descriptions for gene using the xref endpoint
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

# get genomic location, most severe consequence and traits
def parse_variant_phenotypes(rs, var):
  r=defaultdict(list)
  r['genomic_location']       = var['mappings'][0]['location']
  r['most_severe_consequence']= var['most_severe_consequence']
  
  trait={}
  for p in var['phenotypes']:
    trait[p['trait']] = 1;
  
  for n in trait:
    r['trait'].append(n)
  return r

## List Returns all tissues currently available in Homo sapiens
ext='/eqtl/tissue/homo_sapiens'
decoded = request(ext)
print (json.dumps(decoded, indent=4, sort_keys=True))

# Examine a variant  
variant = 'rs2736340'
# Generic information
ext='/variation/human/%s?phenotypes=1' %(variant)
decoded = request(ext)

# genomic location, most severe consequence and traits   
r = parse_variant_phenotypes(variant, decoded)
pprint.pprint(r)
#print(json.dumps(r, indent=4, sort_keys=True))
  
# Find Regulatory Features in this area
ext='/overlap/region/human/%s?feature=regulatory' %(r['genomic_location'])
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


  

"""
{
  "MAF": 0.361422, 
    "ambiguity": "Y", 
    "ancestral_allele": "C", 
    "evidence": [
      "Frequency", 
    "HapMap", 
    "1000Genomes", 
    "Cited", 
    "Phenotype_or_Disease"
      ], 
    "mappings": [
    {
      "allele_string": "C/T", 
      "assembly_name": "GRCh38", 
      "coord_system": "chromosome", 
      "end": 11486464, 
      "location": "8:11486464-11486464", 
      "seq_region_name": "8", 
      "start": 11486464, 
      "strand": 1
    }
  ], 
    "minor_allele": "T", 
    "most_severe_consequence": "regulatory_region_variant", 
    "name": "rs2736340", 
    "phenotypes": [
    {
      "genes": "BLK", 
      "pvalue": "3.00e-7", 
      "risk_allele": "T", 
      "source": "NHGRI-EBI GWAS catalog", 
      "study": "PMID:21408207", 
      "trait": "SYSTEMIC LUPUS ERYTHEMATOSUS", 
      "variants": "rs2736340"
    }, 
"""
