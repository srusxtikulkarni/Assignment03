wallet = int(input("Enter wallet amount:"))
purchase = int(input("Enter purchase amount"))
wallet -= purchase
print("Wallet Balance:", wallet)

#Increment score
score = 10
print("Before increment Score:",score)
score += 5
print("Updated Score:", score)

#Reduce stock
stock = int(input("Enter stock:"))
sold = int(input("Enter sold stock:"))
stock -= sold
print("Remaining Stock:", stock)
