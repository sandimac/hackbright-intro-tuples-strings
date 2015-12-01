#my_name = "Alexis"
# print my_name.split()

#letters = []

#for i in my_name:
#	letters.append(i)
#print letters

#my_num = "1, 2, 3, 4, 5"

#print my_num.split(",")

#my_fish = "One fish Two fish Red fish Blue fish"
#my_fish +=" " 
#fish_list = my_fish.split(" fish ")
#fish_list.pop()
#print fish_list


#str = "item:apples, quantity:4, price:1.50\n"

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n"]


def break_list(str):
	split_str = str.split(",")
	quantity = float(split_str[1].split(":")[1])
	price = float(split_str[2].split(":")[1])
	return (quantity, price)


def calculate_one_bill(quantity, price):
	return quantity * price

total_price = 0
for i in items:
	q, p = break_list(i)
	total_price += calculate_one_bill(q, p)

	
# print calculate_one_bill(q, p)
print total_price