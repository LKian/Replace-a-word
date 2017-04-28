entirety = raw_input("Enter all text to search: ").lower()
word_to_find = raw_input("What word do you want to find? " ).lower()
replacement = raw_input("What would you like to replace it with?: ")
newsentence = entirety.replace(word_to_find,replacement)
print newsentence
words = newsentence.split()
count=0
for i in words:
	if i==replacement:
		count+=1
print count,"instances of \"", word_to_find,"\" were replaced with \"",replacement,"\"."