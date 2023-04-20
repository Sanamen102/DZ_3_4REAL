products=["bread", "milk", "bananas", "meat"]
count = len(products)
for i in range(count):
    if len(products[i])%2==0:
        print(products[i])