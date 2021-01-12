price = int(input())
if price >= 300:
    price *= 0.7
elif price >= 250:
    price *= 0.8
elif price >= 100:
    price *= 0.9
elif price < 100:
    price *= 0.95

print(price)