def computepay():
	try:
	  hours = int(input("Enter Hours: "))
	  rate = int(input("Enter Rate: "))
	  if hours > 40: 
		  final = hours - 40
		  newrate = rate * 1.5
		  add = final * newrate
		  pay = 400 + add
		  print("Pay ", pay)
	  else:
		  print("Pay: ", pay)
	except (ValueError):
		  print("Error, please enter numeric input.")
	
computepay()
