cname = input("Please enter the customer's name: ")

gprice = input("Please enter the unit price for the goods: ")

gnum = input("Please enter the number of goods purchased: ")

gname = input("Please enter the name of the goods: " )

tot = float(gprice) * float(gnum)

print("The customer", cname, "paid $" + str(tot), "for", gnum, "items of", gname)
