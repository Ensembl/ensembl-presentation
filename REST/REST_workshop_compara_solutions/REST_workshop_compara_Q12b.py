import requests, sys, json
server = "https://rest.ensembl.org"


# Homology endpoint exercises

# Q12b: Return only the unaligned chimp and mouse homologs for the gene given in 1a in json format

ext = "/homology/id/ENSG00000229314?target_species=chimp;target_species=mouse;aligned=0"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
decoded = r.json()
print json.dumps(decoded, indent=4, sort_keys=True)
print ("\n------->>>>Q12b Return only the unaligned chimp and mouse homologs for the gene given in 1a in json format. !!!!! \n\n\n")
