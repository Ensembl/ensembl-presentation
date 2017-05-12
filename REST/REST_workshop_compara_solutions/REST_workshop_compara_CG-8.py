import requests, sys, json
server = "https://rest.ensembl.org"


# Gene tree endpoint exercises

# CG-8: Get the gene tree predicted for the human gene with the symbol HOXD4-001 in simple nh format.

ext = "/genetree/member/symbol/human/HOXD4-001?"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>> Q8: Get the gene tree predicted for the human gene with the symbol HOXD4-001 in simple nh format.!!!!! \n\n\n\n")
