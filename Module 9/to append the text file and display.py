string = input("Enter string to be appended: ")
with open("C:/Users/Acer/Documents/to count no of lines in text file.py", 'a') as file:
    file.write(string)

with open("C:/Users/Acer/Documents/to count no of lines in text file.py", "r") as file:
    print(file.read())
