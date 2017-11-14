from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, ensembl_rest

server = "http://rest.ensembl.org"


## Export all microarray platforms that are annotated for humans in Ensembl and their associated information.
request='/regulatory/species/homo_sapiens/microarray'
decoded = ensembl_rest.get_endpoint(server, request)
print(json.dumps(decoded, indent=4, sort_keys=True))

"""
  You have performed a microarray experiment with the array HumanWG_6_V2. The following probes gave you a positive signal: 
  ILMN_1763508, ILMN_1861090, ILMN_1890175, ILMN_1749304, ILMN_1894173, ILMN_1911643, ILMN_1891089, ILMN_1859810, ILMN_1843473,  ILMN_1770856
    a) Which transcripts do they map to? 
    b) Which genes do these transcripts belong to?
"""

# Transcript and gene mappings for different probes
array = 'HumanWG_6_V2'
probes = ['ILMN_1763508', 'ILMN_1861090', 'ILMN_1890175', 'ILMN_1749304', 'ILMN_1894173', 'ILMN_1911643', 'ILMN_1891089', 'ILMN_1859810', 'ILMN_1843473', 'ILMN_1770856']
for probe in probes:
  print(probe)
  request='/regulatory/species/homo_sapiens/microarray/%s/probe/%s?content-type=application/json;gene=1;transcript=1' %(array, probe)
  decoded  = ensembl_rest.get_endpoint(server, request);
  if decoded:
    print("Probe length: %sbp Sequence: %s" %(decoded['probe_length'], decoded['sequence']))
    if decoded['transcripts']:
      for tr in decoded['transcripts']:
        print("Transcribt Stable ID: %s Gene Stable ID: %s Gene External Name: %s Transcript Description: %s" %( tr['stable_id'], tr['gene']['stable_id'], tr['gene']['external_name'], tr['description']))
    else:
      print("No transcripts mappings found")
  else:
    print("Not found")
  print()
    

