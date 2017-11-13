import json, ensembl_rest
server = "http://rest.ensembl.org"

# Alignment endpoint exercise

# CG-2a: Get in json format the aligned human mammal epo alignment for region 2:106040000-106040050:1

ext = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))