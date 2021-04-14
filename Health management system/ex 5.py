import datetime
def getdate():
    import datetime
    return datetime.datetime.now()
while (True):
    print("Welcome to health management system")
    print("Write 1 for Harry, 2 for Rohan, 3 for Hammad")
    name = int(input())


    if name==1:
        print("Write 1 for log and 2 for retrieve")
        action = int(input())
        if action==1:
            print("Write 1 for food and 2 for exercise")
            foex = int(input())
            if foex==1:
                print("Write the value")
                value = input()
                with open("harryfood.txt", "a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")

                print("Successfully written")
            elif foex==2:
                print("Write the value")
                value = input()
                with open("harryexercise.txt", "a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")
                print("Successfully written \n")
            else:
                print("Invalid command \n")
        elif action==2:
            print("Write 1 for food and 2 for exercise")
            foex = int(input())
            if foex == 1:
                with open("harryfood.txt", "rt") as f:
                    for i in f:
                        print(i, end="")
            elif foex == 2:
                with open("harryexercise.txt", "rt") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("Invalid command \n")
        else:
            print("Invalid command")




    if name==2:
        print("Write 1 for log and 2 for retrieve")
        action = int(input())
        if action==1:
            print("Write 1 for food and 2 for exercise")
            foex = int(input())
            if foex == 1:
                print("Write the value")
                value = input()
                with open("rohanfood.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + value + "\n")

                print("Successfully written")
            elif foex==2:
                print("Write the value")
                value = input()
                with open("rohanexercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully written \n")
            else:
                print("Invalid command \n")
        elif action==2:
            print("Write 1 for food and 2 for exercise")
            foex = int(input())
            if foex==1:
                with open("rohanfood.txt", "rt") as f:
                    for i in f:
                        print(i, end="")
            elif foex==2:
                with open("rohanexercise.txt", "rt") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("Invalid command \n")
        else:
            print("Invalid command")




    if name == 3:
        print("Write 1 for log and 2 for retrieve")
        action = int(input())
        if action == 1:
            print("Write 1 for food and 2 for exercise")
            foex = int(input())
            if foex == 1:
                print("Write the value")
                value = input()
                with open("hammadfood.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + value + "\n")

                print("Successfully written")
            elif foex == 2:
                print("Write the value")
                value = input()
                with open("hammadexercise.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully written \n")
            else:
                print("Invalid command \n")
        elif action == 2:
            print("Write 1 for food and 2 for exercise")
            foex = int(input())
            if foex == 1:
                with open("hammadfood.txt", "rt") as f:
                    for i in f:
                        print(i, end="")
            elif foex == 2:
                with open("hammadexercise.txt", "rt") as f:
                    for i in f:
                        print(i, end="")
            else:
                print("Invalid command \n")
        else:
            print("Invalid command")