Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2), (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
>>> 
>>> ##1. Robin Hood is famous for hitting an arrow with another arrow. Find the coordinates of the points where an arrow hits another arrow.
>>> for i in range (1,len(points)):
    if points[i-1] == points[i]:
        print ("The coordinates of the points where an arrow hits another arrow is: ", points[i])

        
The coordinates of the points where an arrow hits another arrow is:  (5, 7)
>>> ##2. Calculate how many arrows have fallen in each quadrant.
>>> Q1 = 0
>>> Q2 = 0
>>> Q3 = 0
>>> Q4 = 0
>>> Others = 0
>>> 
>>> for i in range (0,len(points)):
    if (points[i][0] > 0) & (points[i][1] > 0):
        Q1 = Q1 + 1
    if (points[i][0] > 0) & (points[i][1] < 0):
        Q2 = Q2 + 1
    if (points[i][0] < 0) & (points[i][1] < 0):
        Q3 = Q3 + 1
    if (points[i][0] < 0) & (points[i][1] > 0):
        Q4 = Q4 + 1
    if (points[i][0] == 0) | (points[i][1] == 0):
        Others = Others + 1

        
>>> print ("In Q1:", Q1)
In Q1: 10
>>> print ("In Q2:", Q2)
In Q2: 2
>>> print ("In Q3:", Q3)
In Q3: 2
>>> print ("In Q4:", Q4)
In Q4: 6
>>> print ("In Others:", Others)
In Others: 2
>>> 
>>> ##3. Find the point closest to the center. Calculate its distance to the center.
>>> 
>>> points_distance = []
>>> minimum_distance = 999999999999
>>> minimum_point = 0
>>> 
>>> for i in range (0,len(points)):
    points_distance.append ((points[i][0]**2 + points[i][1]**2)**0.5)

    
>>> for i in range (0,len(points)):
    if points_distance[i] < minimum_distance:
        minimum_distance = points_distance [i]
        minimum_point = minimum_point + 1

        
>>> print ("Distance to the center of each point:", points_distance)
Distance to the center of each point: [6.4031242374328485, 2.0, 8.06225774829855, 3.1622776601683795, 3.605551275463989, 6.4031242374328485, 3.605551275463989, 8.602325267042627, 8.602325267042627, 2.8284271247461903, 6.4031242374328485, 2.0, 8.06225774829855, 3.1622776601683795, 3.605551275463989, 6.4031242374328485, 3.605551275463989, 8.602325267042627, 8.602325267042627, 2.8284271247461903, 12.727922061357855, 12.041594578792296]
>>> print ("The closest point to the center is point number", minimum_point)
The closest point to the center is point number 2
>>> 
>>> ##4. If the archery target has a radius of 9, calculate the number of arrows that won't hit the target.
>>> In_target = 0
>>> Off_target = 0
>>> radius = 9
>>> 
>>> for i in range (0,len(points_distance)):
    if points_distance[i] <= radius:
        In_target = In_target + 1

        
>>> for i in range (0,len(points_distance)):
    if points_distance[i] > radius:
        Off_target = Off_target + 1

        
>>> print ("Number of arrows that hit the target:", In_target)
Number of arrows that hit the target: 20
>>> print ("Number of arrows that don't hit the target:", Off_target)
Number of arrows that don't hit the target: 2
>>> 
