far = float(input("Please enter the tempereature (fahrenheit):"))
cel = (far - 32) * (5/9)
print("The temperature " + str(format(far, ".2f")) + " degrees Fahrenheit is " + str(format(cel, ".2f")) + " degrees Celsius")