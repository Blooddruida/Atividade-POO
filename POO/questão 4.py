popA = 80.000
popB = 200.000
cresA = 0.03  # 3%
cresB = 0.015  # 1.5%
anos = 0
while popA < popB:
    popA += popA * cresA
    popB += popB * cresB
    anos += 1
print(f"Em {anos} anos a população de A irá ultrapassar a população de B.")
