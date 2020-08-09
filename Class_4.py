# Conditional Statements

# Conditional if:
# Question that return a True or False.

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

#______________________________________________#

# Other way:

x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#_____________________________________________#

# Using elif and else:

x = 20

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')

#_________________________________________________#

#Except: Can be use when we want to avoid an error.

#_________________________________________________#

#Exercise:

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h < float(40):
    print(h*r)
else:
    print(((h - float(40))*float(1.5)*r) + (float(40)*r))

#_______________________________________________________#

#Exercise

score = input("Enter Score: ")
score = float(score)
if score > float(0.0) and score < float(1.0):
    if score >= float(0.9):
        print('A')
    elif score >= float(0.8):
        print('B')
    elif score >= float(0.7):
        print('C')
    elif score >= float(0.6):
        print('C')
    elif score < float(0.6):
        print('F')
else:
    print('Out of range')
