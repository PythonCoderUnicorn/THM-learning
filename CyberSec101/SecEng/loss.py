

# SLE = AssetValue × EF 
# asset_value = float(input("Enter value: "))
# exposure_factor = float(input("Enter exposure factor (%): "))/100

# SLE = asset_value * exposure_factor
# print(f"SLE = ${SLE}")


# ARO_before = float(input("Enter annual rate of occurence (ARO): "))

# ALE_before = SLE * ARO_before
# print("ALE (before) = ${:,}".format(ALE_before))

# exposure_factor_after = float(input("Enter EF after safeguard (%): "))/100

# SLE_after = asset_value * exposure_factor_after
# print(f"SLE (after) = ${SLE_after}")


# ARO_after = float(input("Enter ARO: "))#/100

# ALE after Safeguard = SLE after Safeguard × ARO after Safeguard
# ALE_after = SLE_after 


# ALE_before 



# asset value
AV = float(input("Enter asset value: "))
# annual rate of occurrence
ARO = float(input("Enter ARO: "))
# exposure factor
EF = float(input("Enter exposure factor (EF): "))
# single loss expectancy
SLE = AV * EF
print(f"Single loss expectancy = ${SLE}")

# loss w/o safeguards
ALE1 = ARO * SLE
print(f"loss w/o safegurads = ${ALE1}")

# annual cost of safeguards
ACS = float(input("Enter safeguard cost: "))

# loss after safeguards
ALE2 = float(input("Enter ALE2: "))

value = ((ALE1 - ALE2) - ACS)

print(f"Value of safeguard = ${value}")




