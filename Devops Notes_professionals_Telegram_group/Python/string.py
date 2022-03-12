#It's all about strings

#Double Quote
double_quote = "This is Double's string"

print double_quote

#escape sequence
single_quote = 'This is Double \'s string'

print single_quote

"""
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash
"""

#Raw String

print(r'That is Carol\'s cat.')

#Indexing and Slicing Strings

#'Hello world!'

#'   H   e   l   l   o       w   o   r   l   d    !   '
#    0   1   2   3   4   5   6   7   8   9   10   11

spam = 'Hello world!'
print spam[0]
print spam[9]
print spam[-1]
print spam[0:5]
print spam[:5]
print spam[6:]
print spam[::-1]
#The in and not in Operators with Strings
print 'Hello' in 'Hello World'
print 'HELLO' in 'Hello World'

print 'cats' not in 'cats and dogs'

#Useful String Methods

#upper() : convert to all upper
print spam.upper()
#lower() convert to all lower case
print spam.lower()

#islower() and isupper()

test = 'COOL'

print test.islower()
print test.isupper()

#Explore of your own on the given string methods : title(), isalpha(), isalnum, isspace(), isdecimal(), startswith(), endswith()

#join()

list = ['my', 'name', 'is', 'deepak']
print ', '.join(list)
print ':::'.join(list)

#split()

var = 'SiddeshDDDwantsDDDtoDDDlearnDDDPython'


var1 = var.split('DDD')

print var1

#Multiline split

Multi = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

print Multi.split('\n')

#explore yourselves the methods strip(), rstrip(), lstrip()
var = '    Mohan     '
trim = var.strip(' ')
print trim
test = 'abc def ghia'
a = test.lstrip('a')
print a

print "Hi" +  " Hurray " + "Bye"

print "Hurray" * 5

if list[4] eq 'Movie':
    print("True")
else:
    print("False")

var_test = "Spicctc"
test = var_test.strip('Scy')



