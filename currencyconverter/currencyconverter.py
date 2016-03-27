import urllib.request
import json

baseUrl = "www.reddit.com/r/"
subreddit = "globaloffensive"
finalUrl = baseUrl + subreddit

def parseLine(line): 
	items = line.split(" ")
	return { 'amount': int(items[0]), 'baseCurrency': items[1], 'targetCurrency': items[3] }

def formatResult(values):
	result = convertCurrency(values["amount"], values["baseCurrency"], values["targetCurrency"])
	return str(values["amount"]) + " in " + values["baseCurrency"] + " equals " + str(result) + " in " + values["targetCurrency"]


def convertCurrency(amount, baseCurrency, targetCurrency):
	completedUrl = "http://api.fixer.io/latest?base=" + baseCurrency + "&symbols=" + targetCurrency
	with urllib.request.urlopen(completedUrl) as currencyData:
		currencyResult = json.loads(currencyData.read().decode('utf-8'))
		rate = (currencyResult['rates'][targetCurrency])
		return rate * amount 

def readFromFile():
	fname = "currencyconverterinput.txt"
	with open(fname) as file:
		lines=file.read().splitlines()
		for line in lines:
			values = parseLine(line)
			print(formatResult(values))

def readFromConsole():
	inputLine = input("bass is a sick cunt: ")
	if inputLine is e
	values = parseLine(inputLine)
	print(formatResult(values))


readFromConsole()
