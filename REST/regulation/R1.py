from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests, json, sys, ensembl_rest

server = "http://rest.ensembl.org"


"""
  Carla
  Fetch from EFO
"""
def efo_request (ext):
  r = requests.get(ext, headers={ "Content-Type" : "application/json"})
  if not r.ok:
    return r.status_code
  decoded = r.json()
  return decoded;

"""
  Carla
  Add HTTP status reason to status id
"""
def http_status_to_string(http_status_code):
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

# 1. List all Epigenomes available in Ensembl Regulation
endpoint='/regulatory/species/homo_sapiens/epigenome'
decoded = ensembl_rest.get_endpoint(server, endpoint, 'application/json')

# 2. Find additional information (where available) for each epigenome using the Ontology Lookup Service 
efo_endpoint = "http://www.ebi.ac.uk/ols/api/ontologies/efo/terms?obo_id="
for r in decoded:

  print("Epigenome name: %s" %r['name'])
  # No EFO ID assigned to this epigenome
  if not r['efo_id']:
    print("No EFO ID assigned: %s\n"%(r['scientific_name']))
    continue

  request = efo_endpoint+r['efo_id']
  efo     = efo_request(request)

  # if the request is not ok, an status code (integer) will be returned
  if type(efo) is int:
    http_string = http_status_to_string(efo);
    print("!!REST Error: efo_id [%s] %s "%(r['efo_id'], http_string) )
    continue

  print_efo(efo)


  
