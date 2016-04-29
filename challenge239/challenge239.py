def isDivisiblebythree(number):
    return number%3 == 0

# if number is divisible by three:
#   print number plus 0
#   continue dividing this new number by three
# elseif if adding one makes number divisible by three
#   print number plus 1
#   add one and continue dividing this new number by three

# else if subtracting one makes number divisible by three
#   print number minus 1
#   subtract one and continue dividing this new number by three

def reducingNumber(number):
    if isDivisiblebythree(number):
        print(str(number) + " 0")
        newNumber = number/3
    elif isDivisiblebythree(number + 1):
        print(str(number) + " 1")
        newNumber = (number + 1) / 3
    else:
        print(str(number) + " -1")
        newNumber = (number - 1) / 3
    
    if newNumber == 1:
        print(newNumber)
    else:
        reducingNumber(newNumber)

fname = "input239.txt"
with open(fname) as file:
    bass=file.read().splitlines()
    for line in bass:
        reducingNumber(int(line))



# else:
#       return False
#           if False
#               ((number() + 1)/3) in integer
#                   return True

#   else: ((number() - 1)/3) in integer
