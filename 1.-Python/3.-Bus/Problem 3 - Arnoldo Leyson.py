Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import statistics
>>> 
>>> stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
>>> 
>>> ## 1. Calculate the number of stops.
>>> print ("Number of stops:", len(stops))
Number of stops: 9
>>> 
>>> ## 2. Assign to a variable a list whose elements are the number of passengers at each stop (in-out).
>>> passengers_on = []
>>> passengers_off = []
>>> passengers_per_stop = []
>>> total_passengers = []
>>> 
>>> bus_capacity = 0
>>> 
>>> for on,off in stops:
    passengers_on.append (on)
    passengers_off.append (off)

    
>>> for i in range (0, len(stops)):
    passengers_per_stop.append (passengers_on[i] - passengers_off[i])

    
>>> total_passengers.append (passengers_per_stop[0])
>>> for i in range (0,len(stops)-1):
    total_passengers.append (total_passengers[i] + passengers_per_stop[i+1])

    
>>> print ("Passengers on", passengers_on)
Passengers on [10, 4, 3, 3, 5, 1, 5, 4, 2]
>>> print ("Passengers off:", passengers_off)
Passengers off: [0, 1, 5, 4, 1, 5, 8, 6, 3]
>>> print ("Passengers per stop:", passengers_per_stop)
Passengers per stop: [10, 3, -2, -1, 4, -4, -3, -2, -1]
>>> print ("Total passengers:", total_passengers)
Total passengers: [10, 13, 11, 10, 14, 10, 7, 5, 4]
>>> 
>>> ## 3. Find the maximum occupation of the bus.
>>> print ("Maximum occupation of the bus:", max(total_passengers))
Maximum occupation of the bus: 14
>>> 
>>> ## 4. Calculate the average occupation. And the standard deviation.
>>> print ("Average occupation of the bus:", sum(total_passengers) / len(total_passengers))
Average occupation of the bus: 9.333333333333334
>>> print ("Standard deviation of the occupation of the bus:", statistics.pstdev(total_passengers))
Standard deviation of the occupation of the bus: 3.197221015541813
>>> 
