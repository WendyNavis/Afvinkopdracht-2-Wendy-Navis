# 1.0 Personal Information
print ("Wendy Navis")
print ("Tulpenstraat 24, Doetinchem, 7004DJ")
print ("0627891669")
print ("Bio-informatics")

# 2.0 Sales Prediction
Verkoop = float(input("Totale verkoop dit jaar is: "))
Profit = Verkoop * 0.23
print ("Profit: ")
print (Profit)

# 3.0 Pounds to Kilograms
Pounds = float(input("Hoeveel pounds? "))
kilograms = Pounds * 0.454
print ("Kilogram: ")
print (kilograms)

# 4.0 Total Purchase
# Deze code vraagt de prijzen voor de items op.
Item_1 = float(input("Prijs van item 1: "))
Item_2 = float(input("Prijs van item 2: "))
Item_3 = float(input("Prijs van item 3: "))
Item_4 = float(input("Prijs van item 4: "))
Item_5 = float(input("Prijs van item 5: "))

#berekent het Subtotal van de aankoop.
Subtotal = Item_1 + Item_2 + Item_3 + Item_4 + Item_5
print ("Subtotal: ")
print (format(Subtotal, ".2f"))

#berekent de hoeveelheid belasting er betaald wordt op de aankoop.
SalesTax = Subtotal * 0.07
print ("Salestax: ")
print (format(SalesTax, ".2f"))

#Berekent het Totale bedrach van de aankoop.
Total = Subtotal + SalesTax
print ("Total: ")
print (format(Total, ".2f"))

