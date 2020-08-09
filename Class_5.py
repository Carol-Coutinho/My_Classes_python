# Class_5: Using functions
# We have to understand that a function needs to be invoke!

#Stored and reused Steps

def thing(): #Def define a function
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

#__________________________________________#
#EX:

def greet (lang):
    if lang == 'es':
        print('Hola')
    if lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('fr')
greet('es')

#_________________________________________#

#Return values

def greet():
    return 'Hello'

print(greet(), "Glenn")

#__________________________________________#

#Ex:

def greet(lang):
    if lang == 'es':
        return 'Hola'
    if lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Carol')
print(greet('es'), 'Dany')
print(greet('fr'), 'Jen')

#____________________________________________#

#Exercise:

def computepay(hrs, rate):
    if hrs > float(40):
        p = (hrs - 40) * 1.5 * rate + 40 * rate
    else:
        p = hrs * rate
    return p

h = input("Enter Hours:")
hrs = float(h)
r = input("Enter Rate:")
rate = float(r)
p = computepay(hrs, rate)
print("Pay", p)
