############################# PYGLATIN ###########################
# 2/11 Ahoy! (or Should I say Ahoyay!)
print "Pig Latin"


# 3/11 Input
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")


# 4/11 Check Yourself!
print 'Welcome to the Pig Latin Translator!'


# Start coding here!
original = raw_input("Enter a word:")

if (len(original) > 0):
    print original
else:
    print "empty"


# 5/11 Check Youself... Some More
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

if (len(original) > 0 and original.isalpha()):
    print original
else:
    print "empty"


# 6/11 Pop Quiz!
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

if (len(original) > 0 and original.isalpha()):
    print original
else:
    print "empty"


# 7/11 Ay B C
pyg = 'ay'


# 8/11 Word Up
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]


# 9/11 Move it on Back
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]

new_word = word + first + pyg


# 10/11 Ending Up
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]

new_word = word + first + pyg
new_word = new_word[ 1:len(new_word) ]


# 11/11
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]

new_word = word + first + pyg
new_word = new_word[ 1:len(new_word) ]