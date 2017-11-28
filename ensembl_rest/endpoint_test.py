import json, ensembl_rest

server = 'http://rest.ensembl.org'

# request = "/family/id/PTHR15573"
# endpoint = ensembl_rest.get_endpoint(server, request) # JSON is default
# print (json.dumps(endpoint, indent=4, sort_keys=True))

request = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals;display_species_set=human;display_species_set=chimp;display_species_set=gorilla"
endpoint = ensembl_rest.get_endpoint(server, request, 'text/xml')
print (endpoint)