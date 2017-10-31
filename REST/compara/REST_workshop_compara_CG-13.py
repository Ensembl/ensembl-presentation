import requests, sys, json
server = "https://rest.ensembl.org"


# Homology endpoint exercises

#Q CG-13: Get all the orthologs human gene with the symbol HOXD4-001 in orthoxml format

ext = "/homology/symbol/human/HOXD4-001?"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-orthoxml+xml"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q13 Get all the orthologs human gene with the symbol HOXD4-001 in orthoxml format. !!!!! \n\n\n")
