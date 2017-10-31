import requests, sys, json
server = "https://rest.ensembl.org"


# Family endpoint exercises

# CG-3b: Get the aligned cdna sequences for only the ensembl members of the family with the stable id PTHR10740_SF4

ext = "/family/id/PTHR10740_SF4?aligned=1;sequence=cdna;member_source=ensembl"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
decoded = r.json()
print (json.dumps(decoded, indent=4, sort_keys=True))
print ("\n------->>>>Q3b Get the aligned cdna sequences for only the ensembl members of the family with the stable id PTHR10740_SF4!!!!! \n\n\n\n")
