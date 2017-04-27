import requests, sys, json
server = "https://rest.ensembl.org"


# cafe tree endpoint exercises

# Q11: Get the cafe tree information for the gene tree predicted for the human gene with the symbol HOXD4-001

ext = "/cafe/genetree/member/symbol/homo_sapiens/HOXD4-001?"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q11 Get the cafe tree information for the gene tree predicted for the human gene with the symbol HOXD4-001!!!!! \n\n\n\n")

