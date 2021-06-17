s = int(input("Enter a no.: "))
i = 0 
with open("C:/Users/Acer/Documents/to write a list in a file.py", 'r') as file:
    for i in range(s):
        print(file.readline())
