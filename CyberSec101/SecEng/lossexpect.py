


# Quantitative Risk Analysis
# Single Loss Expectancy

# Using quantitative analysis, we need to assign monetary values and numeric percentages.
# single loss expectancy SLE is the loss incurred due to the realization of threat
# Exposure Factor (EF) is the percentage of loss a realised threat can cause to an asset.


# SLE = AssetValue × EF 
# SLE = ($10,000 laptop) * (90% risk of ransomware) = $9000



asset_value = float(input("Enter value: "))
exposure_factor = float(input("Enter exposure factor (%): "))/100

SLE = asset_value * exposure_factor
print(f"SLE = ${SLE}")




# Annualised Loss Expectancy

# ALE is loss of company expects to lose per year due to threat
# ARO  annualized rate of occurrence is the expected number of times this threat 
#      is realized (frequency per year)

# laptop infected with ransomware every 2 yrs = ARO 0.5
# $9000 * 0.5 = cost us $4500 per laptop per year unless we take proper measures.

# ALE before Safeguard = SLE before Safeguard × ARO before Safeguard 
# ALE before = SLE before × ARO before
# ALE before = $9000 × 0.5 = $4,500.

# ALE = SLE * ARO


ARO_before = float(input("Enter annual rate of occurence (ARO): "))

ALE_before = SLE * ARO_before
print("ALE (before) = ${:,}".format(ALE_before))







# ALE after Safeguard = SLE after Safeguard × ARO after Safeguard


# SLE after Safeguard = AssetValue × EF after Safeguard

# exposure factor (EF) is not expected to change. = exposure_factor


# antivirus would significantly decrease the annualised rate of occurrence (ARO).
# say ARO = 0.02
# ARO_after = float(input("Enter ARO: "))/100


# SLE after Safeguard = AssetValue × EF after Safeguard 
# SLE after safeguard = $10,000 × 90% = $9,000.
SLE_after = asset_value * exposure_factor
print(f"SLE (after) = ${SLE_after}")





# ALE_after Safeguard = SLE_after Safeguard × ARO_after Safeguard = $9,000 × 0.02 = $180.
ALE_after = SLE_after * ARO_before #ARO_after
print(f"ALE (after) = ${ALE_after}")


# ALE_post_safeguard = SLE * ARO
# print("ALE post safeguard = ${:,}".format(ALE_post_safeguard))



# estimated the safeguard cost to be $120 per year.

safeguard_cost = float(input("Enter cost of safeguard: "))

# ValueofSafeguard = ALEbeforeSafeguard − ALEafterSafeguard − AnnualCostSafeguard

# ValueofSafeguard = $4,500 − $180 − $120 = $4,200
safeguard_value = ALE_before - ALE_after - safeguard_cost

print("safeguard value = ${:,}".format(safeguard_value))


# ALE before == Loss Value

# ALE_before - ALE_after - safeguard_cost













# value of the selected safeguard is positive = approve
#  value of the safeguard = negative, the cost > benefits (not justified)

if safeguard_value > 0:
  print(" proceed with project")
if safeguard_value <0:
  print(" reject project")



