age = 31
month = 11
# Error
# print('My age is ' + str(age) + ' years old')

# Convert from int to string
print('My age is ' + str(age) + ' years old')

# Return Array
print('My age is {0} years old'.format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} "
      .format(31, "January", "March", "May", "July",
              "August", "October", "December"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("My ages is %d years old" % age)
print("My age is %d %s, %d %s" % (age, "years", month, "months"))

# Using space format
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print('PI is approximately %12.50f' % ( 22 / 7))

# Another using space format
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# Space will decrease
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print('PI is approximately {0:12.50f}'.format( 22 / 7))

print("January: {2}, February: {0}, March: {2}, April: {1}, May: {2}, June: {1}, July: {2}, August: {2}, September: {1}, October: {2}, November: {1}, December: {2}".format(28, 30, 31))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))