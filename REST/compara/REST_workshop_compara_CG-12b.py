import json, ensembl_rest
server = "http://rest.ensembl.org"

# Homology endpoint exercises

#Q CG-12b: Return only the unaligned chimp and mouse homologs for the gene given in 1a in json format

ext = "/homology/id/ENSG00000229314?target_species=chimp;target_species=mouse;aligned=0"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))