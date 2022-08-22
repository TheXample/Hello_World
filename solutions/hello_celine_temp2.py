import re

def selectNumber():
    number = input("input number: ")
    if(re.match("[0-9][0-9]*", number) != None):
        number = int(number)
        return int(number)
    else:
        return selectNumber

def selectOperation():
    operation = input("please choose add/subtract/multiply/divide: ")
    if (re.match("(add)|(subtract)|(multiply)|(divide)", operation) != None):
        return operation
    return selectOperation

def select():
    numberOne = selectNumber()
    numberTwo = selectNumber()
    operation = selectOperation()
    return [numberOne, numberTwo, operation]

def execute(numberOne, numberTwo, operation):
    result = "Your result: "
    if(operation == "add"):
        result += str(numberOne + numberTwo)
    elif(operation == "subtract"):
        result += str(numberOne - numberTwo)
    elif(operation == "multiply"):
        result += str(numberOne * numberTwo)
    elif(operation == "divide") :
        result += str(numberOne / numberTwo)
    return result

userInput = input("Do you want to use the calculater? [yes/no] ")

while(userInput != "no"):
    selectedValues = select()
    print(execute(selectedValues[0], selectedValues[1], selectedValues[2]))
    userInput = input("Do you want to use the calculater? [yes/no] ")