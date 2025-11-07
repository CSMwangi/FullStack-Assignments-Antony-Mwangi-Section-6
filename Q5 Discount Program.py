product = input("Enter product name: ")
price = float(input("Enter product price: "))

if price > 10000:
    discounted_price = price * 0.8
elif 5000 <= price <= 10000:
    discounted_price = price * 0.9
else:
    discounted_price = price

print(f"The {product} now costs {discounted_price} KES after discount.")
