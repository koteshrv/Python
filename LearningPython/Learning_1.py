from math import *

name = "Kotesh"
age = "20"
Height = "174"
Weight = "80"
print(name + " is " + age + " years old. " + "His height is " + Height + "cm and weight is " + Weight + "kgs")
print("Now he is learning Python")
phrase = "Kotesh is learning Python"
print(phrase.lower())               # prints the string in lowercase
print(phrase.upper())               # prints the string in uppercase
print(phrase.isupper())             # prints true if the phrase is in uppercase
print(phrase.islower())             # prints true if the phrase is in lowercase
print(phrase.upper().isupper())     # prints true but it does not changes the original data
print(phrase.lower().islower())     # prints true but it does not changes the original data
print(len(phrase))                  # prints the length of the number
print(phrase.index("P"))            # prints where is char P is located
print(phrase.index("Python"))       # prints the value of the initial index
print(phrase.replace("Kotesh", "Koteswararao"))
num = 500
print(str(num) + " is an integer")  # when we are using a number in a string, It should be converted to str
print(pow(5, 2))                    # power function
print(max(500, 1000))               # max function
print(min(500, 1000))               # min function
print(round(3.7))                   # rounds the value
print(floor(3.6))                   # floor function
print(ceil(3.3))                    # ceil function
print(sqrt(2500))                   # square root
name = input("Enter your name here :    ")
print("Hi " + name + "!")
names = ["Kotesh", "Koti", "Koteswararao", "KHHV Koteswararao"]      # list
#          0,-4     1,-3       2,-2                3,-1
print(names)
print(names[-2])                                # accessing a list
print(names[1:])                                # prints the elements of list from 1
print(names[1:3])                               # prints the elements from 1 to 2 i.e 1 to n - 1
names[1] = "Venky"
print(names[1])
print(names)
names.sort()                                    # sorts the list
print(names)
primes = [2, 3, 5, 7, 11, 13]
names.extend(primes)                            # extends the list
print(names)
names.append("Ko")                              # appends the list
print(names)
names.insert(1, "Karri Hari Hara Venkata Koteswararao")
print(names)
names.remove("Ko")                              # removes an element in the list
print(names)
names.pop()                                     # pops the list i.e removes the last element in the list
print(names)
print(names.index("Kotesh"))                    # index of the list element
print(names.count("Kotesh"))                    # prints number of times Kotesh is repeated in the list
names.clear()                                   # clears the entire list
print(names)
names = ["Kotesh", "Koti", "Koteswararao", "KHHV Koteswararao"]
names_dummy = names.copy()                      # copies the list into another list
print(names_dummy)
number_tuple = (1, 2, 3)                        # tuple representation
# Key difference between lists and tuples are tuples are immutable i.e once they are assigned the value of the tuple
# cannot be assigned as we do in lists
# If we try to assign a value to the tuple it will return 'tuple' object does not support item assignment


status = False
if status:
    print("Status is true")
else:
    print("Status is false")

log = 0

if status or log == 0:
    print("Passed as log value is 0")

if not status and log == 0:
    print("Status is true and log value is zero")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions["Feb"])      # we can also use monthConversions.get("Dec")


for i in range(10):
    print(i)                        # prints 0 to 9

# range(n) gives values from 0 to n - 1
# range(1, n) gives values from 1 to n - 1

print(2**6)                         # '**' can also be used instead of pow function

try:
    a = 10 / 0
    num = int(input("Enter any number here :    "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

myFile = open("data.txt", "r")
print(myFile.readable())            # prints true is it is in read mode
# print(myFile.readline())            # reads a single line in the file
# print(myFile.readlines())           # reads all lines in the file

for line in myFile.readlines():
    print(line)

myFile.close()


myFile = open("data.txt", "a")
myFile.write("\nNow I'm using Pycharm")
myFile.close()

myFile = open("data.txt", "r")
for line in myFile.readlines():
    print(line)
myFile.close()


newFile = open("dataset.txt", "w")
newFile.write("Kotesh is learning Python from 2 hours")
newFile.close()









