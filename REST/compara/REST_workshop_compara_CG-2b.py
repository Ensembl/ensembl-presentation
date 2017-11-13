import json, ensembl_rest
server = "http://rest.ensembl.org"

# Alignment endpoint exercise

# CG-2b: display only the [human, chimp, gorilla] alignment of the mammal epo alignment for region 2:106040000-106040050:1.  output in phyloxml

ext = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals;display_species_set=human;display_species_set=chimp;display_species_set=gorilla"
content_type = "text/xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)