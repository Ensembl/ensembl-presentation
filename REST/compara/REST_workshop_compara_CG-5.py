import json, ensembl_rest
server = "http://rest.ensembl.org"

# Family endpoint exercises

# CG-5: Get the information for uniprot members of families predicted for the human gene with the symbol HOXD4-201. Show no alignments and no sequences

ext = "/family/member/symbol/human/HOXD4-201?aligned=0;sequence=none;member_source=uniprot"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))