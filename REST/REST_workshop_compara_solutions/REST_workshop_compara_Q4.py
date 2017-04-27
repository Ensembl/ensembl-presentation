import requests, sys, json
server = "https://rest.ensembl.org"


# Family endpoint exercises

# Q4: Get the information for families predicted for the human gene ENSG00000283087. What do you notice?

ext = "/family/member/id/ENSG00000283087?"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
decoded = r.json()
print json.dumps(decoded, indent=4, sort_keys=True)
print ("\n------->>>>Q4 Get the information for families predicted for the human gene ENSG00000283087. What do you notice?!!!!! \n\n\n\n")
