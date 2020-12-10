Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> "1. Assign the challenge data to variables with representative names: well_height, daily_distance, nightly_distance and snail_position."
'1. Assign the challenge data to variables with representative names: well_height, daily_distance, nightly_distance and snail_position.'
>>> well_height = 125
>>> daily_distance = 30
>>> nightly_distance = 20
>>> snail_position = -125
>>> 
>>> "2. Create a variable days to keep count of the days that pass until the snail escapes the well."
'2. Create a variable days to keep count of the days that pass until the snail escapes the well.'
>>> days = 0
>>> 
>>> "3. Find the solution to the challenge using the variables defined above."
'3. Find the solution to the challenge using the variables defined above.'
>>> while snail_position <0:
	for i in range(1,):
		if (snail_position ==0) | (snail_position <0):
			snail_position = snail_position + daily_distance
			days = days + 1
			if (snail_position ==0) | (snail_position <0):
				snail_position = snail_position - nightly_distance	
			elif (snail_position >0):
				snail_position = snail_position
		else: 
			snail_position = snail_position

			
>>> "4. Print the solution."
'4. Print the solution.'
>>> print ("Number of days the snail needs to get out of the well: ", days)
Number of days the snail needs to get out of the well:  11
>>> 
