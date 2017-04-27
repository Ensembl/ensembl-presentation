import requests, sys, json
server = "https://rest.ensembl.org"


# Gene tree endpoint exercises

# Q7: Get the gene tree predicted for the gene ENSG00000189221 in full nh format

ext = "/genetree/member/id/ENSG00000189221?nh_format=full"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q7 Get the gene tree predicted for the gene ENSG00000189221 in full nh format!!!!! \n\n\n\n")
