with open("harry.txt") as f:
    a = f.readlines()
    print(a)

f = open("harry.txt", "rt")
b = f.readlines()
print(b)
# Question of the day - Yes or No and why?
# Ans - Yes it will print because after using with open block the file is closed and then we again open the file so it will print
f.close()
