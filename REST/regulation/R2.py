from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, ensembl_rest

server = "http://rest.ensembl.org"



## List all Epigenomes we currently have in the regulatory build
request = '/regulatory/species/homo_sapiens/epigenome'
decoded = ensembl_rest.get_endpoint(server, request)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get ENSG for ESPN Gene  
request = "/xrefs/symbol/homo_sapiens/espn"
decoded = ensembl_rest.get_endpoint(server, request)
print("Retrieving Ensembl Gene ID for ESPN gene")
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get the coordinates for ESPN gene  
ensg = decoded[0]['id']
request = "/lookup/id/%s?condensed=1" %ensg
decoded = ensembl_rest.get_endpoint(server, request)
print("Getting coordinates")
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get region 1000bp upstream  
chro  = decoded['seq_region_name']
start = decoded['start']
start = start-1000
end   = decoded['start']

# Find Regulatory Features in this area
request='/overlap/region/human/%s:%s-%s?feature=regulatory' %(chro, start, end)
decoded = ensembl_rest.get_endpoint(server, request)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get more information about the RegulatoryFeature, see in which Epigenomes it is active  
ensr = decoded[0]['ID']
request='regulatory/species/homo_sapiens/id/%s?activity=1' %ensr

# Coordinates of the Feature
chro  = decoded[0]['seq_region_name']
start = decoded[0]['start']
end   = decoded[0]['end']

# Find motifs within the Regulatory Feature
request='/overlap/region/human/%s:%s-%s?feature=motif' %(chro, start, end)
decoded = ensembl_rest.get_endpoint(server, request)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Find Variations in the motif  
for motif in decoded:
  chro  = motif['seq_region_name']
  start = motif['start']
  end   = motif['end']
  request='/overlap/region/human/%s:%s-%s?feature=variation' %(chro, start, end)
  decoded  = ensembl_rest.get_endpoint(server, request);
  if decoded:
    print("Motif:%s [%s:%s:%s] Strand: %s" %(motif['binding_matrix'], motif['seq_region_name'], motif['start'], motif['end'], motif['strand']))
    print(json.dumps(decoded, indent=4, sort_keys=True))

