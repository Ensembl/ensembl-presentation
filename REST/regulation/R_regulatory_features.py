from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys
# server = "http://test.rest.ensembl.org"
server = "http://0:3000/"


# Used for resolving requests and decode the JSON
def request (ext):
  r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
  if not r.ok:
    r.raise_for_status()
    sys.exit()
  decoded = r.json()
  return decoded;

## List all Epigenomes we currently have in the regulatory build
ext='/regulatory/species/homo_sapiens/epigenome'
decoded = request(ext)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get ENSG for ESPN Gene  
ext = "/xrefs/symbol/homo_sapiens/espn"
decoded = request(ext)
print("Retrieving Ensembl Gene ID for ESPN gene")
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get the coordinates for ESPN gene  
ensg = decoded[0]['id']
ext = "/lookup/id/%s?condensed=1" %ensg
decoded = request(ext)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get region 1000bp upstream  
chro  = decoded['seq_region_name']
start = decoded['start']
start = start-1000
end   = decoded['start']

# Find Regulatory Features in this area
ext='/overlap/region/human/%s:%s-%s?feature=regulatory' %(chro, start, end)
decoded = request(ext)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Get more information about the RegulatoryFeature, see in which Epigenomes it is active  
ensr = decoded[0]['ID']
ext='regulatory/species/homo_sapiens/id/%s?activity=1' %ensr

# Coordinates of the Feature
chro  = decoded[0]['seq_region_name']
start = decoded[0]['start']
end   = decoded[0]['end']

# Find motifs within the Regulatory Feature
ext='/overlap/region/human/%s:%s-%s?feature=motif' %(chro, start, end)
decoded = request(ext)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Find Variations in the motif  
for motif in decoded:
  chro  = motif['seq_region_name']
  start = motif['start']
  end   = motif['end']
  ext='/overlap/region/human/%s:%s-%s?feature=variation' %(chro, start, end)
  decoded  = request(ext);
  if decoded:
    print("Motif:%s [%s:%s:%s] Strand: %s" %(motif['binding_matrix'], motif['seq_region_name'], motif['start'], motif['end'], motif['strand']))
    print(json.dumps(decoded, indent=4, sort_keys=True))

