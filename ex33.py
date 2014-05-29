


maximum = int(raw_input("What should the max be?"))
increase = int(raw_input("By what should the numbers increase?"))

def count_up(max, incr):
	i = 0
	numbers = []
	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + incr
		print "number now: ", numbers
		print "At the bottom i is %d" % i
	print "The numbers: "

	for num in numbers:
		print num

count_up(maximum, increase)

