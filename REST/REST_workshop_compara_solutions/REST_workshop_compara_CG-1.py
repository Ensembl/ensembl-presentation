import requests, sys, json
server = "https://rest.ensembl.org" #http://ebi-cli-003:3000"


# Alignment endpoint exercise

# CG-1a: Get in json format the LastZ pairwise alignment for taeniopygia_guttata V gallus_gallus for region 2:106041430-106041480:1

ext = "/alignment/region/taeniopygia_guttata/2:106041430-106041480:1?method=LASTZ_NET;species_set=taeniopygia_guttata;species_set=gallus_gallus"
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
decoded = r.json()
print json.dumps(decoded, indent=4, sort_keys=True)
print ("\n------->>>> Q1 Get in json format the LastZ pairwise alignment for taeniopygia_guttata V gallus_gallus for region 2:106041430-106041480:1!!!!! \n\n\n\n")

