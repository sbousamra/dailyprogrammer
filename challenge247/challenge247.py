

def parseLine(line): 
	items = line.split(" ")

	return { 'batteryVoltage': int(items[0]), 'batteryCapacity': int(items[1]), 'ledVoltage': float(items[2]), 'ledCurrent': int(items[3]), 'time': int(items[4]) }

def formatResult(values):
	resultLed = maxLed(values["batteryVoltage"], values["batteryCapacity"], values["ledVoltage"], values["ledCurrent"], values["time"])
	resultResistance = resistor(values["batteryVoltage"], values["batteryCapacity"], values["ledVoltage"], values["time"])
	resultDisplay = ("*--|>|---|>|---|>|---|>|---|>|--*" * round(resultLed/serialDisplay(values["batteryVoltage"], values["ledVoltage"])))

	return "You can light " + str(resultLed) + " lights in total in series" + " with a resistance of " + str(resultResistance) + " in a format such as : " + str(resultDisplay)

def maxLed(batteryVoltage, batteryCapacity, ledVoltage, ledCurrent, time):
	maxSerial = round(batteryVoltage/ledVoltage)
	maxLights = ((batteryCapacity/ledCurrent)/time) * maxSerial

	return maxLights

def serialDisplay(batteryVoltage, ledVoltage):
	ledAmount = round(batteryVoltage/ledVoltage)
	return ledAmount	

def resistor(batteryVoltage, batteryCapacity, ledVoltage, time):
	#Ohm's Law I = (V/R)	
	batteryCapacityAmps = (batteryCapacity/1000)/time
	remainingVoltage = batteryVoltage%ledVoltage
	resistance = remainingVoltage/batteryCapacityAmps

	return resistance

def readFromConsole():
	inputLine = input("enter your battery voltage, battery capacity, LED voltage, LED current and the time you want it lighted for: ")

	values = parseLine(inputLine)
	print(formatResult(values))

readFromConsole()