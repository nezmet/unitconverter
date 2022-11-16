# Unit Converter
print("          Unit Converter")
print(" ===================================")

unit_dict = {1: "Celcius to Fahrenhiet", 2: "Fahrenhiet to Celcius", 3: "Celcius to Kelvin", 4: "Kelvin to Celcius" , 5: "Kelvin to Fahrenhiet" , 6: "Fahrenhietto Kelvin" , 7: "Gallon to Quart" , 8: "Quart to Gallon" , 9: "Gallon to Pint" , 10: "Pint to Gallon" , 11: "Quart to Pint" , 12: "Pint to Quart" , 13: "Cup to Fluid Ounce" , 14: "Fluid Ounce to Cup" , 15: "Tablespoon to Teaspoon" , 16: "Teaspoon to Tablespoon" , 17: "Liter to Mililiter" , 18: "Mililiter to Liter" , 19: "Pound to Ounce" , 20: "Ounce to Pound" , 21: "Gram to Kilogram" , 22: "Kilogram to Gram"}

value = float(input("Enter the number you want to convert: "))
for keys, values in unit_dict.items():
    print("{:2}. {}".format(keys, values))

convert = int(input("\nSelect the conversion you want to do from 1 to 22: "))

if convert == 1:
    print("{} Celcius is equal to {} Fahrenhiet.".format(value, value*1.8+32))

elif convert == 2:
    print("{} Fahrenhiet is equal to {} Celcius.".format(value,(value-32)*0.556))
    
elif convert== 3:
    print("{} Celcius is equal to {} Kelvin.".format(value , value+273.15))
    
elif convert== 4:
    print("{} Kelvin equal to {} Celcius.".format(value , value-273.15))
    
elif convert== 5:
    print("{} Kelvin equal to {} Fahrenhiet.".format(value , (value-273.15)*1.8+32))
    
elif convert== 6:
    print("{} Fahrenhiet equal to {} Kelvin.".format(value , (value-32)*0.556+273.15))    

elif convert== 7:
    print("{} US Liquid Gallon equal to {} US Liquid Quart.".format(value , value*4))

elif convert== 8:
    print("{} US Liquid Quart equal to {} US Liquid Gallon.".format(value , value*0.25))
    
elif convert== 9:
    print("{} US Liquid Gallon equal to {} US Liquid Pint.".format(value , value*8))
    
elif convert== 10:
    print("{} US Liquid Pint equal to {} US Liquid Gallon.".format(value , value*0.125))
    
elif convert== 11:
    print("{} US Liquid Quart equal to {} US Liquid Pint.".format(value , value*2))
    
elif convert== 12:
    print("{} US Liquid Pint equal to {} US Liquid Quart.".format(value , value*0.5))
    
elif convert== 13:
    print("{} US Legal Cup equal to {} US Fluid Ounce.".format(value , value*8.115))
    
elif convert== 14:
    print("{} US Fluid Ounce equal to {} US Legal Cup.".format(value , value/8.115))
    
elif convert== 15:
    print("{} US Tablespoon equal to {} US Teaspoon.".format(value , value*3))
    
elif convert== 16:
    print("{} US Tablespoon equal to {} US Teaspoon.".format(value , value/3))
    
elif convert== 17:
    print("{} Liter equal to {} Mililiter.".format(value , value*1000))
    
elif convert== 18:
    print("{} Mililiter equal to {} Liter.".format(value , value/1000))
    
elif convert== 19:
    print("{} Pound equal to {} Ounce.".format(value , value*16))
    
elif convert== 20:
    print("{} Ounce equal to {} Pound.".format(value , value/16))
    
elif convert== 21:
    print("{} Gram equal to {} Kilogram.".format(value , value/1000))
    
elif convert== 22:
    print("{} Kilogram equal to {} Gram.".format(value , value*1000))

else:
    print("Sorry, Please type correct number from 1 to 22.")

print("Good Luck Cooking!" )