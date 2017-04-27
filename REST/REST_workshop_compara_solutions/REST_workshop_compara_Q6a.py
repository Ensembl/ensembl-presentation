import requests, sys, json
server = "https://rest.ensembl.org"


# Gene tree endpoint exercises

# Q6a: Get the information for the protein genetree with the stable id ENSGT00390000003602. output should be in the orthoxml format

ext = "/genetree/id/ENSGT00390000003602?"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-orthoxml+xml"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q6a Get the information for the protein genetree with the stable id ENSGT00390000003602. output should be in the orthoxml format!!!!! \n\n\n\n")
