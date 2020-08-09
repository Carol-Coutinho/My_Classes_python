# Class_2: Expressions

#Constants:

print(123) # 123 is a constant
print("Hello world") #Hello world is a constant

# Reserved words: you can not use reserved words as variables.
# Ex: if, for, return, while, function ...

#Variables: place where we can store data. That data is store in memory.

x = 12.2 # x is a variable.
y = 14 # y is a variable.

# OBS: you can change the value of the variable in a later statement.

x = 100 # Right now, x is equal to 100 and not 12.2 like before.

# Rules for variables names:
# Must start with a letter or undescore_
# Is case Sensitive

#Sentences or lines:

x = 2 # Assignment statement
x = x+2 #Assignment with expression
print(x) # Print statement function

# Numeric expressions

xx = 2
xx = xx + 2 #Addition
print(xx)

yy = 440 * 12 # Multiplication
print(yy)

zz = yy/ 1000 #Division
print(zz)

jj = 23
kk = jj % 5 #Remainder
print(kk)

print(4**3) #Power

#Precedence Rules:
#1.Parenthesis
#2.Power
#3.Addition
#4.Left to Right

#OBS: Addition can be used with str.
#Ex:

ee = 'hello' + 'world'
print(ee)

# But careful, python don't understand de addition of diferent classes,
# like:

eee = 'Hello' + 1 # It won't work.

# We can change the class of a variable with functions, like:
# float(), int()

# Input function: read data

nam = input('Who are you?')
print('Welcame', nam)

#OBS: Important to note that the value that we put on the Input
# will be a str!
