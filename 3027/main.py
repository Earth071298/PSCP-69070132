"""Cal the length of barbed wire. """

width, length, layers = map(int,input().split())
price_per_meter = int(input())

total_length = ((width*2) + (length*2))*layers
price = total_length*price_per_meter

print(total_length)
print(price)
