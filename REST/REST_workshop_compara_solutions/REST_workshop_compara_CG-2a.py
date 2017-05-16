import requests, sys, json
server = "https://rest.ensembl.org"


# Alignment endpoint exercise

# CG-2a: Get in json format the aligned human mammal epo alignment for region 2:106040000-106040050:1

ext = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
decoded = r.json()
print (json.dumps(decoded, indent=4, sort_keys=True))
print ("\n------->>>> Q2a Get in json format the aligned human mammal epo alignment for region 2:106040000-106040050:1!!!!! \n\n\n\n")
