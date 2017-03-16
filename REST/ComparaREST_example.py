import requests, sys
 
import requests, sys
 
server = "http://ebi-cli-003:3000"
ext = "/homology/id/ENSG00000278500?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print repr(decoded)

print ("\n------->>>> Above we retrieve the orthologs of  the hox gene !!!!! \n\n\n")

ext = "/genetree/id/ENSGT00840000130527?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
print (r.text)

print ("\n------->>>> Above we retrieve the gene tree that human HOX D4 is a member using the gene tree id!!!!! \n\n\n")


ext = "/genetree/member/id/ENSG00000278500?aligned=1"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print repr(decoded)

print ("\n------->>>> Above we retrieve the gene tree using a HOX D4 human gene member stable id!!!!! \n\n\n")


ext = "/family/id/PTHR24326_SF118?member_source=ensembl;sequence=none;aligned=0"

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()

decoded = r.json()
print repr(decoded)


print ("\n------->>>> Above we retrieve the family that HOX D4 is a member using the family id!!!!! \n\n\n")

ext = "/family/member/id/ENSGALP00000037899?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print repr(decoded)

print ("\n------->>>> Above we retrieve the HOX D4 family using the chicken seq member id!!!!! \n\n\n")


#ext = "/family/member/symbol/homo_sapiens/HOX?aligned=0;sequence=none;member_source=ensembl"
ext = "/family/member/symbol/homo_sapiens/HOXD4-001?aligned=0;sequence=none;member_source=ensembl"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print repr(decoded)

print ("\n------->>>> Above we retrieve the family using the symbol for the human HOX D4 gene!!!!! \n\n\n")

ext = "/cafe/genetree/id/ENSGT00840000130527?"
#ENSGT00730000110903?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()


print (r.text)

print ("\n------->>>> Above we retrieve the cafe tree that HOX D4 is a member using the gene tree id!!!!! \n\n\n")


ext = "/cafe/genetree/member/id/ENSG00000189221?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
#r = requests.get(server+ext, headers={ "Content-Type" : "text/x-nh"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print (repr(decoded))

#print (r.text)

print ("\n------->>>> Above we retrieve the cafe tree that HOX D4 is a member using the gene stable id!!!!! \n\n\n")

ext = "/cafe/genetree/member/symbol/homo_sapiens/HOXD4-001?"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print repr(decoded)

print ("\n------->>>> Above we retrieve the cafe tree using the HOX D4 symbol!!!!! \n\n\n")


