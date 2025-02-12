claims = [ ("denied", 673), ("approved", 348), ("approved", 232),
    ("approved", 143), ("approved", 268), ("denied", 424), 
    ("approved", 298), ("approved", 175), ("approved", 423), 
    ("approved", 214), ("denied", 498), ("approved", 154), 
    ("denied", 663), ("approved", 379), ("approved", 249), 
    ("approved", 481), ("denied", 488), ("denied", 496), 
    ("denied", 620), ("denied", 316), ("denied", 625), 
    ("approved", 398), ("approved", 384), ("approved", 351), 
    ("approved", 260), ("approved", 142), ("approved", 437), 
    ("denied", 602), ("denied", 699), ("approved", 498), 
    ("approved", 432), ("denied", 331), ("denied", 213), 
    ("denied", 602), ("denied", 231), ("approved", 315), 
    ("approved", 308), ("approved", 188), ("approved", 195), 
    ("approved", 229), ("approved", 408), ("approved", 228), 
    ("approved", 143), ("denied", 212), ("approved", 264), 
    ("approved", 283), ("denied", 301), ("denied", 493), 
    ("approved", 173), ("denied", 271) ]
#a
claim_numbers = [claim[1] for claim in claims]

total_claim_numbers = sum(claim_numbers)

print(total_claim_numbers)

#b
approved_claims = sum([claim[1] for claim in claims if claim[0] == "approved"])

print(approved_claims)

#c
approved_claims_total = [claim[1] for claim in claims if claim[0] == "approved"]

denied_claims_total = [claim[1] for claim in claims if claim[0] == "denied"]

print(sum(approved_claims_total))
print(sum(denied_claims_total))

#d
approved_claims = [claim for claim in claims if claim[0] == "approved" and 250 <= claim[1] <= 500]
number_of_approved_claims = len(approved_claims)

print(number_of_approved_claims)

#e
approved = [claim for claim in claims if claim[0] == "approved" and claim[1] > 300]
denied= [claim for claim in claims if claim[0] == "denied" and claim[1] > 300]

approved_claims = len(approved)
denied_claims = len(denied)

print(f"{approved_claims}")
print(f"{denied_claims}")