from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, ensembl_rest

server = "http://rest.ensembl.org"

 
## List all Epigenomes we currently have in the regulatory build
endpoint='/regulatory/species/homo_sapiens/epigenome'
decoded = ensembl_rest.get_endpoint(server, endpoint, 'application/json')
#print(json.dumps(decoded, indent=4, sort_keys=True))


"""
  Fetch from EFO
"""
efo_endpoint = "http://www.ebi.ac.uk/ols/api/ontologies/efo/terms?obo_id="
def efo_request (ext):
  r = requests.get(ext, headers={ "Content-Type" : "application/json"})
  if not r.ok:
    return r.status_code
  decoded = r.json()
  return decoded;

"""
  Add HTTP status reason to status id
"""
def http_to_string(http_status):
  reason = requests.status_codes._codes[http_status]
  string = "HTTP status code: %s. HTTP Reason: %s" %(http_status, reason) 
  return string 


"""
  Pretty printing of EFO  
"""
def print_efo (efo):
  print("Link(URL): %s" %(efo['_links']['self']['href']))
  for t in efo['_embedded']['terms']:
    print("Link(IRI): %s" %(t['iri']))
    if t['description']:
      for d in t['description']:
        print("Description: %s" %(d))
    else: 
      print('No description provided')
  print()


"""
  main
"""
for r in decoded:

  print("Epigenome name: %s" %r['name'])
  if not r['efo_id']:
    print("No EFO ID assigned: %s\n"%(r['scientific_name']))
    continue

  ext =efo_endpoint+r['efo_id']
  efo = efo_request(ext)
  if not efo:
    print("No EFO ID assigned: %s\n"%(efo_id))
    continue

  if type(efo) is int:
    http_string = http_to_string(efo);
    print("!!REST Error: efo_id [%s] %s "%(r['efo_id'], http_string) )
    continue

  print_efo(efo)


  
