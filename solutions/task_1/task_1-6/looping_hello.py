password = "password"
userInput = input("Please enter password: ")
if(userInput == password):
    while(userInput != "Stop" and userInput != "stop"):
        userInput = input("please choose eather 1: Hello or 2: Bye now: ")
        if(userInput == "Stop" or userInput == "stop"):
            print("Stopping")
        elif(userInput == "1"):
            print("Hello")
        elif(userInput == "2"):
            print("Bye")