import json, ensembl_rest
server = "http://rest.ensembl.org" #http://ebi-cli-003:3000"


# Alignment endpoint exercise

# CG-1: Get in json format the LastZ pairwise alignment for taeniopygia_guttata V gallus_gallus for region 2:106041430-106041480:1

ext = "/alignment/region/taeniopygia_guttata/2:106041430-106041480:1?method=LASTZ_NET;species_set=taeniopygia_guttata;species_set=gallus_gallus"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# CG-2a: Get in json format the aligned human mammal epo alignment for region 2:106040000-106040050:1

ext = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# CG-2b: display only the [human, chimp, gorilla] alignment of the mammal epo alignment for region 2:106040000-106040050:1.  output in phyloxml

ext = "/alignment/region/human/2:106040000-106040050:1?method=EPO;species_set_group=mammals;display_species_set=human;display_species_set=chimp;display_species_set=gorilla"
content_type = "text/xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)

# -------------------------------------------------------------------------------------------------- #

# Family endpoint exercises

# Q CG-3a: Get the information for the family with the stable id PTHR10740_SF4

ext = "/family/id/PTHR10740_SF4"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# Q CG-3b: Get the aligned cdna sequences for only the ensembl members of the family with the stable id PTHR10740_SF4

ext = "/family/id/PTHR10740_SF4?aligned=1;sequence=cdna;member_source=ensembl"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# Q CG-4: Get the information for families predicted for the human gene ENSG00000283087. What do you notice?

ext = "/family/member/id/ENSG00000283087?"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# Q CG-5: Get the information for uniprot members of families predicted for the human gene with the symbol HOXD4-201. Show no alignments and no sequences

ext = "/family/member/symbol/human/HOXD4-201?aligned=0;sequence=none;member_source=uniprot"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))


# -------------------------------------------------------------------------------------------------- #

# Gene tree endpoint exercises

# Q CG-6a: Get the information for the protein genetree with the stable id ENSGT00390000003602. output should be in the orthoxml format

ext = "/genetree/id/ENSGT00390000003602?"
content_type = "text/x-orthoxml+xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)

# Q CG-6b: Get the NcRNA gene tree with the stable id RF01168. output in phyloxml format with sequences aligned

ext = "/genetree/id/RF01168?aligned=1;sequence=cdna"
content_type = "text/x-phyloxml+xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)

# Q CG-7: Get the gene tree predicted for the gene ENSG00000189221 in full nh format

ext = "/genetree/member/id/ENSG00000189221?nh_format=full"
content_type = "text/x-nh"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)

# Q CG-8: Get the gene tree predicted for the human gene with the symbol HOXD4-201 in simple nh format.

ext = "/genetree/member/symbol/human/HOXD4-201"
content_type = "text/x-nh"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)


# -------------------------------------------------------------------------------------------------- #


# CAFE tree endpoint exercises

# Q CG-9: Get the cafe tree information for the genetree with the stable id ENSGT00390000003602. output should be in the json format.

ext = "/cafe/genetree/id/ENSGT00390000003602"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# Q CG-10: Get the cafe tree for gene tree predicted for the gene ENSG00000189221 in nh format. Notice anything?

ext = "/cafe/genetree/member/id/ENSG00000189221"
content_type = 'text/x-nh'
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)

# Q CG-11: Get the cafe tree information for the gene tree predicted for the human gene with the symbol HOXD4-201

ext = "/cafe/genetree/member/symbol/homo_sapiens/HOXD4-201"
content_type = 'text/x-nh'
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)


# -------------------------------------------------------------------------------------------------- #


# Homology endpoint exercises

# Q CG-12a: Get all the homologues for the human gene ENSG00000229314 in xml format

ext = "/homology/id/ENSG00000229314?"
content_type = "text/xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)

# Q CG-12b: Return only the unaligned chimp and mouse homologs for the gene given in 1a in json format

ext = "/homology/id/ENSG00000229314?target_species=chimp;target_species=mouse;aligned=0"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))

# Q CG-13: Get all the orthologs human gene with the symbol HOXD4-201 in orthoxml format

ext = "/homology/symbol/human/HOXD4-201"
content_type = "text/x-orthoxml+xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)