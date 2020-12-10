Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> well_height = 125
>>> daily_distance = 30
>>> nightly_distance = 20
>>> snail_position = -125
>>> days = 0
>>> while snail_position <0:
	for i in range(1,):
		if (snail_position <0):
			snail_position = snail_position + daily_distance
			days = days + 1
			if (snail_position <0):
				snail_position = snail_position - nightly_distance	
			elif (snail_position ==0) | (snail_position >0):
				snail_position = snail_position
		else: 
			snail_position = snail_position

			
>>> print ("Number of days the snail needs to get out of the well: ", days)
Number of days the snail needs to get out of the well:  11
>>> 
