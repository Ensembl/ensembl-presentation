import requests, sys, json
server = "https://rest.ensembl.org"


# Alignment endpoint exercise

# CG-2b: display only the [human, chimp, gorilla] alignment of the mammal epo alignment for region 2:106040000-106040050:1.  output in phyloxml

ext = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals;display_species_set=human;display_species_set=chimp;display_species_set=gorilla"
r = requests.get(server+ext, headers={ "Content-Type" : "text/xml"})
if not r.ok:
  r.raise_for_status()
  sys.exit()
print (r.text)
print ("\n------->>>> Q2b display only the [human, chimp, gorilla] alignment of the mammal epo alignment for region 2:106040000-106040050:1.  output in phyloxml!!!!! \n\n\n\n")

