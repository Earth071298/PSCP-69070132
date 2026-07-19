"""promotion"""

promotion_person = int(input())
pay_person = int(input())
price = int(input())
person  = int(input())

promotion_set = person // promotion_person
left = person % promotion_person

pay_promotion = (promotion_set * pay_person) + left
total = pay_promotion * price

print(total)
