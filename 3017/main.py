"""service charge 10% and vat 7% cal"""

price = int(input())

service_charge = price * (10/100)
if service_charge < 50 :
    total = price + 50
elif service_charge > 1000 :
    total = price + 1000
else :
    total = price + service_charge

vat = total * (7/100)
bill_total = total + vat

print(f"{bill_total:.2f}")
