#FOURTH ASSIGNMENT
#TAKE HOME ASSIGNMENT ON LOOP
#Number 1. A loop statement to print out numbers between 1 & 20.
numbers=2
while numbers<=19:
            print(f"{numbers} is a number between 1 and 20") 
            numbers+=1   
#Number 2. A loop statement to print out even numbers between 30 & 70.
start, end = 30, 70
for value in range(start, end + 1):
        if value%2 ==0:
            print(value, end ="\n")
            
            
 #Number 3. A loop ststement to print out multiplication table 5.           
num = 5
for i in range(1, 13):
    print(num, 'x', i, '=' ,num*i)

# Number 4. A program that accepts user input and prints out the factorial 
# of the number.
fac_num =int(input("Enter a prefered number to compute the factorial:"))

factorial = 1

# check if the number is negative, positive or zero
if fac_num < 0:
   print("Number is negative and factorial does not exist")
elif fac_num == 0:
   print("The factorial of 0 is always 1")
else:
   for i in range(1,fac_num + 1):
       factorial = factorial*i
   print("The factorial of",fac_num,"is",factorial)


# ASSIGNMENT ON DICTIONARY METHODS AND ITS IMPLEMENTATION  
      
# fromkeys():This method returns a dictionary with a specified key and value.
# implemantation:
# 1.It creates a dictionary from a sequence of keys
alpha = {'b', 'f', 'j', 't', 'z' }
alphabet = dict.fromkeys(alpha)
print(alphabet)

# 2. It creates a dictionary from a sequence of keys with value
alpha = {'b', 'f', 'j', 't', 'z' }
value = 'single letter'
alphabet = dict.fromkeys(alpha, value)
print(alphabet)

# 3.This method creates a dictionary from mutable object list
alpha= {'b', 'f', 'j', 't', 'z' }
value = [5]
alphabet = dict.fromkeys(alpha, value)
print(alphabet)
value.append(10)
print(alphabet)


# get():The get() method returns the value for the specified
# key if key is in dictionary.
# Implimentation:
vegetable = {'fruits':'watermelon', 'colour':'red'}
print('Fruits: ', vegetable.get('fruits'))
print('Colour: ', vegetable.get('colour'))

# When the value is not provided
print('Carrot: ', vegetable.get('carrot'))

# When the value is provided
print('Carrot: ', vegetable.get('carrot', 5)) 

   
# item():This method returns a view object that displays a list of 
# dictionary's (key, value) tuple pairs.
# implementation:
fruits = { 'strawberry': 2, 'watermelon': 3, 'banana': 4 }
print(fruits.items()) 

   
# keys():The keys() method returns a view object that displays a list of
# all the keys in the dictionary.
# implementation:
family = {'fathers_name': 'Tom', 'age': 50, 'salary': 5000.0}
print(family.keys())


# pop():This method removes and returns an element from a dictionary 
# having the given key.
# implimentation:
# When it Pops an element from the dictionary
houses = { 'bungalow': 2, 
          'duplex': 5, 
          'hut': 7 
          }
house_type = houses.pop('duplex')
print('The popped element is:', house_type)
print('The dictionary is:', houses)

#The method when it Pops an element not present from the dictionary,
# it provides a default value.
houses = { 'bungalow': 2, 'oduplex': 5, 'hut': 7 }
house_type = houses.pop('semi_detached', 'storey_building')
print('The popped element is:', house_type)
print('The dictionary is:', houses)


#popitem():The popitem() method removes and returns the last element 
# (key, value) pair inserted into the dictionary.
# implementation:
person = {'name': 'Nora', 
          'age': 20, 
          'salary': 10000.0
          }
result = person.popitem()
print('Return Value = ', result)
print('person = ', person)


# setdefault():The setdefault() method returns the value of a key 
# (if the key is in dictionary). If not, it inserts key with a  
# value to the dictionary.
# implementation:
# using the setefault() when key is in the dictionary
family = {'mothers_name': 'Tina', 'age': 40}
age = family.setdefault('age')
print('Person = ',family)
print('Age = ',age)
# using setdefault() when key is not in the dictionary
person = {'name': 'Jude'}
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)


# Update():The update() method updates the dictionary with the elements
# from another dictionary object or from an iterable key/value pairs.
# implementation:
x = {1: "one", 2: "five"}
x1 = {2: "two"}

# updates the value of key 2
x.update(x1)
print(x)

x1 = {3: "three"}
# this will add a new element with key 3
x.update(x1)
print(x)


# values():This method returns a view object that displays a
# list of all the values in the dictionary.
# implementation:
fruit = { 'pineapple': 20, 'cherry': 10, 'orange': 15 }
print(fruit.values())  


# ASSIGNMENT ON THE USE OF append() METHOD
# A program that append items in apple list to fruit list using append method.
Fruits = ["apple"]
Apple= ["apple1", "apple2", "apple3", "apple4"]
for i in Apple:
        print(i)
        Fruits.append(i)
        print(Fruits)






