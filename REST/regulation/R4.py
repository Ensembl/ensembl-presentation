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

## List all Microarrays we currently have in the regulatory build
ext='/regulatory/species/homo_sapiens/microarray'
decoded = request(ext)
print(json.dumps(decoded, indent=4, sort_keys=True))

# Transcript and gene mappings for different probes
array = 'HumanWG_6_V2'
probes = ['ILMN_1763508', 'ILMN_1861090', 'ILMN_1890175', 'ILMN_1749304', 'ILMN_1894173', 'ILMN_1911643', 'ILMN_1891089', 'ILMN_1859810', 'ILMN_1843473', 'ILMN_1770856']
for probe in probes:
  print(probe)
  ext='/regulatory/species/homo_sapiens/microarray/%s/probe/%s?content-type=application/json;gene=1;transcript=1' %(array, probe)
  decoded  = request(ext);
  if decoded:
    print("Probe length: %sbp Sequence: %s" %(decoded['probe_length'], decoded['sequence']))
    if decoded['transcripts']:
      for tr in decoded['transcripts']:
        print("Transcript: %s Stable ID: %s Gene: %s (%s)" %(tr['description'], tr['display_id'], tr['gene']['stable_id'], tr['gene']['external_name']))
    else:
      print("No transcripts mappings found")
  else:
    print("Not found")
  print()
    


