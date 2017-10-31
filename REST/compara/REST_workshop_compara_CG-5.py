import requests, sys, json
server = "https://rest.ensembl.org"


# Family endpoint exercises

# CG-5: Get the information for uniprot members of families predicted for the human gene with the symbol HOXD4-001. Show no alignments and no sequences

ext = "/family/member/symbol/human/HOXD4-001?aligned=0;sequence=none;member_source=uniprot"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit() 
decoded = r.json()
print (json.dumps(decoded, indent=4, sort_keys=True))
print ("\n------->>>>Q5 Get the information for uniprot members of families predicted for the human gene with the symbol HOXD4-001. show no alignments and no sequences!!!!! \n\n\n\n")
