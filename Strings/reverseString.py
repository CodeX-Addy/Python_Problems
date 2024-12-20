# input string
string = "python practice"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	# apending reversed words to l
	l.append(i)
# printing reverse words
print(" ".join(l))
