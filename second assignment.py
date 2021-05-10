#Number 1
x='1000'
y=int(1000)
print(y)
#Number 2
p=3.764
z=int(3.764)
print(z) 
#number 3
num1=99.45
num2=str(99.45)
k='$'+ num2 
s= k + ' ' + 'dollars'
print(s)
#Number 4
#The type()funtion in python returns the data type of the object
#passed to it as an argument. The type()function helps to define 
#the class type of the variable given as input.
#Number 5
#Boolean is a data type that is used to test whether the result of
#an expression is true or false.
#Its two possible values are the two constant objects false and true.
#Number 6
#The % symbol in python is called the modulo operator. It returns 
#the remainder of a dividing the left hand operand by the right hand operand.
#It is an arithmetic operation that is used to get the remainder
#of a division problem.
#Number 7
fancy_name='Mba Chinenye Juliet'
print(fancy_name)
print('\n')
#Number 8
hours=int(input("input hours: ")) * 3600
print(hours)
#Number 9
def easy_money():
    return 100
def best_food_ever():
    return 'sushi'
print(easy_money())
print(best_food_ever())
convert_to_currency=str(input('Type a single number:'))
print('$' + convert_to_currency)
#Nunmber 10
a=str(input('a word!'))
b=str(input('another word!'))
string_adder=(a+' '+b) 
if len(string_adder)>0:
    print(string_adder)   
else:
    print("")
#Number 11
long_word=str(input('Type in any word of your choice:'))
if len(long_word)>7:
    print('True')
else:
    print('False')
#Number 12  
same_first_and_last_letter=str(input('Type in a word:'))
if same_first_and_last_letter[0]==same_first_and_last_letter[-1]:
    print('True')
else:
    print('false')
   #number 13
first_three_characters=str(input('Type your words!'))
print(first_three_characters[0:3])     
