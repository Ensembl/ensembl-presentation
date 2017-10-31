import requests, sys, json
server = "https://rest.ensembl.org"


# cafe tree endpoint exercises

# Q CG-10: Get the cafe tree for gene tree predicted for the gene ENSG00000189221 in nh format. Notice anything?

ext = "/cafe/genetree/member/id/ENSG00000189221?"
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>>Q10 Get the cafe tree for gene tree predicted for the gene ENSG00000189221 in nh format. Notice anything?!!!!! \n\n\n\n")
