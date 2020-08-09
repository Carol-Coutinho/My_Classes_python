#Class_6: Loopd and Interactions

# Repeted Steps

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)

# In this case, WHILE n > 0 the loop will continue, till we reach
# the value of zero, ending the loop.

# We can use the break statment to stop a infinit loop.
#Ex:

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

# The continue statment ends the current interation and jumps
# to the top of the loop and starts the next interation.
#Ex:

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

 # Definite Loops:
 # Using the for statement.

 for i in [5,4,3,2,1]:
     print(i)
print('Blastoff')

# In this case, we are saying print each element(i) of the list
# and then get out of the loop and print 'Blastoff'.

#Ex:

friends = ['Jhon', 'Glenn', 'Carol']
for friend in friends:
    print('Happy New Year', friend)
print('Done')

# Ex: Finding the largest value:

largest_so_far = -1
print ('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 13]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#Ex: Counting in a loop:

zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

#Ex: Search using a Boolean Variable:

found = False
print ('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

#Ex: Finding the smallest value:

smallest = None
print ('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

#Exercise: 
#Write a program that repeatedly prompts a user for integer
#numbers until the user enters 'done'. Once 'done' is entered,
#print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with
#a try/except and put out an appropriate message and ignore the
#number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))

done(largest,smallest)
