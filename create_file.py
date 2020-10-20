import string

f = open(testfile, "a")
for i in range(int(1e4)):
	line = ""
	for j in range(100):
		line = line + random.choice(string.ascii_letters)
	f.write(line)
f.close()
