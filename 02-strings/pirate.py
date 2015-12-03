pirate = {
	"sir": "matey", 
	"hotel": "fleabag inn", 
	"student": "swabbie", 
	"boy": "matey", "madam": 
	"proud beauty", "professor": 
	"foul blaggart", "restaurant": 
	"galley", "your": "yer", 
	"excuse" : "arr", 
	"students":"swabbies", 
	"are":"be", 
	"lawyer": "foul:blaggart", 
	"the": "th'", 
	"restroom": "head", 
	"my": "me", 
	"hello": "avast", 
	"is": "be", 
	"man": "matey"
}

sentence = raw_input("Type a sentence: ")
split_sentence = sentence.split()

for user_word in split_sentence:
	if user_word in pirate:
		print pirate[user_word],
	else:
		print user_word,


