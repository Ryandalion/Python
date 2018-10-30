 # Function that converts and prints fahrenheit to celsius

fahrenheit = 0;
celsius = 0;
print("Celsius ----- Fahrenheit");
for x in range (0,21,1):
    fahrenheit = (((9/5) * celsius) + 32);
    print(celsius,"            ", format(fahrenheit,'.2f'));
    fahrenheit = 0;
    celsius += 1;