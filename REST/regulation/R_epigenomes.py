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


# Print information about each epigenome
efo_server = "http://www.ebi.ac.uk/"
def efo_request (ext):
  r = requests.get(efo_server+ext, headers={ "Content-Type" : "application/json"})
  if not r.ok:
    return
  decoded = r.json()
  return decoded;
for r in decoded:
  if not r['efo_id']:
    print("No EFO ID assigned: %s\n"%(r['scientific_name']))
    continue
  
  print("Scientific Name: %s(%s)" %(r['scientific_name'],r['efo_id']))
# Query EFO 
  ext='ols/api/ontologies/efo/terms?obo_id=%s' %(r['efo_id'])
  efo_decoded = efo_request(ext)
  if not efo_decoded:
    print("No EFO ID assigned: %s\n"%(r['efo_id']))
    continue

  print("Link(URL): %s" %(efo_decoded['_links']['self']['href']))
  for t in efo_decoded['_embedded']['terms']:
    print("Link(IRI): %s" %(t['iri']))
    if t['description']:
      for d in t['description']:
        print("Description: %s" %(d))
    else: 
      print('No description provided')
  print()


