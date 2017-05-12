import requests, sys, json
server = "https://rest.ensembl.org"


# Homology endpoint exercises

# Q CG-12a: Get all the homologues for the human gene ENSG00000229314 in xml format

ext = "/homology/id/ENSG00000229314?"
r = requests.get(server+ext, headers={ "Content-Type" : "text/xml"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q12a Get all the homologues for the human gene ENSG00000229314 in xml format!!!!! \n\n\n")
