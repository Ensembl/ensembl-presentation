import requests, sys, json
server = "https://rest.ensembl.org"


# cafe tree endpoint exercises

# Q9: Get the cafe tree information for the genetree with the stable id ENSGT00390000003602. output should be in the json format.

ext = "/cafe/genetree/id/ENSGT00390000003602?"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit() 
decoded = r.json()
print json.dumps(decoded, indent=4, sort_keys=True)
print ("\n------->>>>Q9 Get the cafe tree information for the genetree with the stable id ENSGT00390000003602. output should be in the json format.!!!!! \n\n\n")
