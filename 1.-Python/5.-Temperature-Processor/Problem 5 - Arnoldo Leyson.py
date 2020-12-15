Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
>>> ##1. Find the minimum temperature of the day and store it in a variable.
>>> min_temp = min(temperatures_C)
>>> print ("The minimum temperature of the day was:", min_temp, "C")
The minimum temperature of the day was: 0 C
>>> 
>>> ##2. Find the minimum temperature of the day and store it in a variable.
>>> max_temp = max(temperatures_C)
>>> print ("The maximum temperature of the day was:", max_temp, "C")
The maximum temperature of the day was: 90 C
>>> ##3. Create a list with the temperatures that are greater than or equal to 70ºC. Store it in a variable.
>>> temp_greater_70 = []
>>> for i in range (0, len(temperatures_C)):
    if temperatures_C [i] >= 70:
        temp_greater_70.append (temperatures_C[i])

        
>>> print ("The temperatures greather or equal to 70 ºC were:", temp_greater_70)
The temperatures greather or equal to 70 ºC were: [70, 76, 80, 81, 80, 83, 90, 79]
>>> 
>>> ##4. Find the average temperature of the day and store it in a variable.
>>> import statistics
>>> print ("The average temperature of the day was:",statistics.mean(temperatures_C), "ºC")
The average temperature of the day was: 60.25 ºC
>>> 
>>> ##5. Imagine that there was a sensor failure at 3am and the data for that specific hour was not recorded. How would you estimate the missing value? Replace the current value of the list at 3am for an estimation.
>>> temp_3am = (temperatures_C[2] + temperatures_C[4]) / 2
>>> temperatures_C[3] = temp_3am
>>> print (temperatures_C)
[33, 66, 65, 62.0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
>>> 
>>> ##6. Bonus: the maintenance staff is from the United States and does not understand the international metric system. Help them by converting the temperatures from Celsius to Fahrenheit.
>>> temperatures_F = []
>>> 
>>> for i in range (0, len(temperatures_C)):
    temperatures_F.append (temperatures_C[i]*1.8 + 32)

    
>>> print (temperatures_F)
[91.4, 150.8, 149.0, 143.60000000000002, 138.2, 140.0, 143.60000000000002, 147.2, 158.0, 168.8, 176.0, 177.8, 176.0, 181.4, 194.0, 174.20000000000002, 141.8, 127.4, 122.0, 120.2, 127.4, 118.4, 113.0, 102.2]
>>> 
>>> ##7. Make a decision!
>>> change_system = 0
>>> if len(temp_greater_70) > 4:
    change_system = change_system + 1

    
>>> temp_above_80 = []
>>> for i in range (0, len(temperatures_C)):
    if temperatures_C[i] > 80:
        temp_above_80.append (temperatures_C[i])

        
>>> if len(temp_above_80) > 0:
    change_system = change_system + 1

    
>>> if statistics.mean(temperatures_C) > 65:
    change_system = change_system + 1

    
>>> if change_system > 0:
    print ("The cooling system needs to be changed")
else:
    print ("The cooling system doesn't need to be changed")

    
The cooling system needs to be changed
>>> 
