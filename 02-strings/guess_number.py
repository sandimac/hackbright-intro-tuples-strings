import random

lower_num = int(raw_input("pick lower range: "))
upper_num = int(raw_input("pick upper range: "))


rand_num = random.randint(lower_num, upper_num)


while True:
	number = int(raw_input("pick a number: "))
	if number < rand_num:
		print "too low!"
	elif number > rand_num:
		print "too high"
	else:
		print "you win!"
		break

