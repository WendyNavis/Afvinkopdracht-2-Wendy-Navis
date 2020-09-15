# 5.0 Distance Traveled
Speed = 70
Hour_6 = 6
Hour_10 = 10
Hour_15 = 15

Distance_6_hours = Speed * Hour_6
Distance_10_hours = Speed * Hour_10
Distance_15_hours = Speed * Hour_15

print ("Distance after: \n 6 hour: ", Distance_6_hours, "
       \n 10 hour: " , Distance_10_hours, "\n 15 hour: ", Distance_15_hours)



# 10.0 Ingredient Adjuster
Number_of_cookies = int(input("How many cookies do you want to make? "))

Recipe_modifier = Number_of_cookies / 48

# Calculates the ingredients needed
Sugar = 1.5 * Recipe_modifier
Butter = 1 * Recipe_modifier
Flour = 2.75 * Recipe_modifier

print ("Ingredienten nodig: ")
print ("Sugar: ")
print (format(Sugar, ".3f"))
print ("Butter: ")
print (format(Butter, ".3f"))
print ("Flour: ")
print (format(Flour, ".3f"))

# 7.0 Miles-per-Gallon
Miles =  int(input("How many miles have you driven?" ))
Gallons =  int(input("How many Gallons did you use to drive those miles? "))

MPG = Miles / Gallons
print ("Miles per gallon: ",(format(MPG, ".3f")))
