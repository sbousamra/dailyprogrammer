fname = "challenge257input.txt"
with open(fname) as file:
	dataLines= file.readlines()[1:]
	dictLines=[]
	for line in dataLines:
		splittedLine=line.split(",")
		birthyear=int(splittedLine[1].strip().split(" ")[2])
		try:
			deathyear=int(splittedLine[3].strip().split(" ")[2])
		except IndexError:
			deathyear = 2016
		yearDict={"birthyear":birthyear, "deathyear":deathyear}
		dictLines.append(yearDict)
	print(dictLines)

	
