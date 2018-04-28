def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)
print('Done')
print('\n\n\n')

#Finding Patterns of Text with Regular Expressions
#The previous phone number–finding program works, but it uses a lot of code to do #something limited: The isPhoneNumber() function is 17 lines but can find only one #pattern of phone numbers. What about a phone number formatted like 415.555.4242 or (415) #555-4242? What if the phone number had an extension, like 415-555-4242 x99? The #isPhoneNumber() function would fail to validate them. You could add yet more code for #these additional patterns, but there is an easier way.
#Regular expressions, called regexes for short, are descriptions for a pattern of text. #For example, a \d in a regex stands for a digit character—that is, any single numeral 0 #to 9. The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same text the #previous isPhoneNumber() function did: a string of three numbers, a hyphen, three more #numbers, another hyphen, and four numbers. Any other string would not match the \d\d\d-\d\d\d-\d\d \d\d regex.
#But regular expressions can be much more sophisticated. For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “Match this pattern three times.” So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches the correct phone number format.


import re

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).
# by putting an r before the first quote of the string value, you can mark the string as a raw string, which does not escape characters. (no double \)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print('\n')

# regex tester: http://www.regexpal.com/

# Adding parentheses will create groups in the regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print('\n')

# matching parenthesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
print('\n')

# Matching multiple groups with pipe
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())
print('\n')
# NOTE: You can find all matching occurrences with the findall() method


# You can also use the pipe to match one of several patterns as part of your regex. 
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
print('\n')


# Optional Matching with the Question Mark
# The ? character flags the group that precedes it as an optional part of the pattern:
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print('\n')

# look for phone numbers that do or do not have an area code:
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
print('\n')


# Matching Zero or More with the Star
# the group that precedes the star can occur any number of times in the text. It can be completely absent or repeated over and over again. 
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
print('\n')


# Matching One or More with the Plus
# While * means “match zero or more,” the + (or plus) means “match one or more.”
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
print('\n')


# Matching Specific Repetitions with Curly Brackets
# For example, the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)
print('\n')


# Greedy and Nongreedy Matching

#Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the previous curly bracket example returns 'HaHaHaHaHa' instead of the shorter possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.
#Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
print('\n')


# The findall() Method
# While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string. 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
nums = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(nums)
print('\n')

# If there are groups in the regular expression, then findall() will return a list of tuples.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
nums2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(nums2, '\n')


# Character Classes

# \d  Any numeric digit from 0 to 9.
# \D  Any character that is not a numeric digit from 0 to 9.
# \w  Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W  Any character that is not a letter, numeric digit, or the underscore character.
# \s  Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S  Any character that is not a space, tab, or newline.

# The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5).

# The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+).
xmasRegex = re.compile(r'\d+\s\w+')
exp = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(exp, '\n')


# Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
v = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(v, '\n')


# You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

# Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () characters with a preceding backslash. For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].

# By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class.
consonantRegex = re.compile(r'[^aeiouAEIOU]')
con = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(con, '\n')


# The Caret and Dollar Sign Characters (beginning, end)
# You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.') == None, '\n')



# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9. 
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None, '\n')

# The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters. 
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None, '\n')


# The Wildcard Character
# You can use the dot-star (.*) to stand in for "anything"
# Remember that the dot character means “any single character except the newline,” and the star character means “zero or more of the preceding character.”
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2), '\n')

# nongreedy fashion, use the dot, star, and question mark (.*?)
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>') # regular, greedy
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group(), '\n')


# Matching Newlines with the Dot Character
# The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group(), '\n')


# REVIEW OF REGEX SYMBOLS:
# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.


# Case-Insensitive Matching
# To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group(), '\n')


# Substituting Strings with the sub() Method
# The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'), '\n')
# Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'), '\n')



# Managing Complex Regexes

# Regular expressions are fine if the text pattern you need to match is simple. But matching complicated text patterns might require long, convoluted regular expressions. You can mitigate this by telling the re.compile() function to ignore whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().
# Now instead of a hard-to-read regular expression like this:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')	
#you can spread the regular expression over multiple lines with comments like this:
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?            # area code
	(\s|-|\.)?                    # separator
	\d{3}                         # first 3 digits
	(\s|-|\.)                     # separator
	\d{4}                         # last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?  # extension
	)''', re.VERBOSE)	
# Note how the previous example uses the triple-quote syntax (''') to create a multiline string so that you can spread the regular expression definition over many lines, making it much more legible.


# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)





# PROJECT: Phone Number and Email Address Extractor
import pyperclip

# Step 1: Create a Regex for Phone Numbers
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                # area code
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

# Step 2: Create a Regex for Email Addresses


emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)

# Step 3: Find All Matches in the Clipboard Text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Step 4: Join the Matches into a String for the Clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')


# e.g., cmd+A, cmd+C: https://www.nostarch.com/contactus.htm



