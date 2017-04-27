import requests, sys, json
server = "https://rest.ensembl.org"


# Gene tree endpoint exercises

# Q6b: Get the NcRNA gene tree with the stable id RF01168. output in phyloxml format with sequences aligned

ext = "/genetree/id/RF01168?aligned=1;sequence=cdna"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-phyloxml+xml"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q6b Get the NcRNA gene tree with the stable id RF01168. output in phyloxml format with sequences aligned!!!!! \n\n\n\n")
