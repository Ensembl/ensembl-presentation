import json, ensembl_rest

server = 'http://rest.ensembl.org'

phenotype_endpoint = '/phenotype/term/homo_sapiens/{}'
variation_post_endpoint = '/variation/human?pops=1'

# 1) Get all variants that are associated with the phenotype 'Coffee consumption'. For each variant print
# a) the p-value for the association
# b) the PMID for the publication which describes the association between that variant and Coffee consumption
# c) the risk allele and the associated gene  

request = phenotype_endpoint.format('coffee consumption')
associations = ensembl_rest.get_endpoint(server, request)

variation2risk_allele = {}
for association in associations:
  variation = association['Variation']
  desc = association['description']
  source = association['source']
  mapped_to_accession = association['mapped_to_accession']
  attributes = association['attributes']
  p_value = attributes['p_value']
  external_reference = attributes['external_reference']
  associated_gene = attributes['associated_gene']
  risk_allele = attributes.get('risk_allele', '')
  if risk_allele !='':
    variation2risk_allele[variation] = risk_allele
  print("Variation: {}, Phenotype: {}, p-value: {}, PMID: {}, Associated gene(s): {}, Risk allele: {}".format
      (variation, desc, p_value, external_reference, associated_gene, risk_allele))


# 2) Extra: Find the most significant association (lowest p-value) for the phenotype 'coffee consumption'
lowest_seen = 1
significant_association = None
for association in associations:
  p_value = float(association['attributes']['p_value'])
  if p_value < lowest_seen:
    lowest_seen = p_value
    significant_association = association

# Error checking, if we found a phenotype, tell us about it
if significant_association:
  print("\n\nThe most significant association is between variant {} and phenotype {}\n".format
          (significant_association['Variation'], 
          significant_association['description']))
  print("p-value: {}\nrisk allele: {}\nassociated gene(s): {}\nexternal reference: {}\n".format(
          significant_association['attributes']['p_value'],
          significant_association['attributes']['risk_allele'],
          significant_association['attributes']['associated_gene'],
          significant_association['attributes']['external_reference']))
  # Remember the value for later, just to make the variable names more readable
  risk_allele = significant_association['attributes']['risk_allele']
else:
# If we don't find any phenotypes, we're doing something wrong
	print("Couldn't find an association for the given phenotype.")
	sys.exit()

# 3) Print the allele frequency for the variants' risk alleles in the Finnish population. 
# The name of the population is 1000GENOMES:phase_3:FIN
variant_ids = list(variation2risk_allele.keys())
params = {'ids' : variant_ids}

variants =  ensembl_rest.post_endpoint(server, variation_post_endpoint, json.dumps(params))

for key, value in variants.items():
  v = variants[key] 
  variant_id = v['name']
  if v['populations']:
    risk_allele = variation2risk_allele[variant_id]
    for population_genotype in v['populations']:
      if population_genotype['population'] in ['1000GENOMES:phase_3:FIN']:
        frequency = population_genotype['frequency']
        allele = population_genotype['allele']
        if allele == risk_allele:
          print("Variant: {}, Allele: {}, Frequency: {}".format(variant_id, allele, frequency))
        else:
          if frequency == 1:
            print("Variant: {}, Allele: {} Frequency: {}".format(variant_id, risk_allele, 0.0))


