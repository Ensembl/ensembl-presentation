import json, ensembl_rest
server = "http://rest.ensembl.org" #http://ebi-cli-003:3000"


# Alignment endpoint exercise

# CG-1a: Get in json format the LastZ pairwise alignment for taeniopygia_guttata V gallus_gallus for region 2:106041430-106041480:1

ext = "/alignment/region/taeniopygia_guttata/2:106041430-106041480:1?method=LASTZ_NET;species_set=taeniopygia_guttata;species_set=gallus_gallus"
endpoint = ensembl_rest.get_endpoint(server, ext) # a third parameter 'content_type' defaults to 'application/json', so no need to define it here
print (json.dumps(endpoint, indent=4, sort_keys=True))