Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import statistics
>>> 
>>> well_height = 125
>>> advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
>>> nightly_distance = 20
>>> snail_position = -125
>>> days = 0
>>> displacement = []
>>> 
>>> while snail_position <0:
    if snail_position <0:
        snail_position = snail_position + advance_cm[days]
        if snail_position <0:
            snail_position = snail_position - nightly_distance
        else:
            snail_position = snail_position
    else:
        snail_position = snail_position
    displacement.append (advance_cm[days] - nightly_distance)
    days = days + 1

    
>>> displacement [-1] = displacement[-1] + nightly_distance
>>> 
>>> print ("Answer 1:")
Answer 1:
>>> print ("Number of days the snail needed to get out of the well:", days, "days")
Number of days the snail needed to get out of the well: 5 days
>>> print ("Answer 2:")
Answer 2:
>>> print ("Maximum displacement in one day:", max(displacement), "centimeters.")
Maximum displacement in one day: 57 centimeters.
>>> print ("Minimum displacement in one day:", min(displacement), "centimeters")
Minimum displacement in one day: 1 centimeters
>>> print ("Answer 3:")
Answer 3:
>>> print ("Average daily progress:", sum(displacement) / len(displacement), "centimeters")
Average daily progress: 25.0 centimeters
>>> print ("Answer 4:")
Answer 4:
>>> print ("Standar deviation of the displacements:", statistics.pstdev(displacement,), "centimeters")
Standar deviation of the displacements: 21.587033144922902 centimeters
>>> 
