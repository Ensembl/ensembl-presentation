import json, ensembl_rest
server = "http://rest.ensembl.org"

# Homology endpoint exercises

# Q CG-12a: Get all the homologues for the human gene ENSG00000229314 in xml format

ext = "/homology/id/ENSG00000229314?"
content_type = "text/xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)