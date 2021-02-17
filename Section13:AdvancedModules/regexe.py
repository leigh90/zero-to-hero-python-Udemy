text = "The agent's phone number is is 408-55-1234"
print("phone" in text)
# import regex library, then pass in the search term to re.search()
# re.search takes in a number of parameters the pattern you are searching for, where to search for it and others
# it returns the start and end index (span) of the search term as well as the match for example <_sre.SRE_Match object; span=(12, 17), match='phone'>

import re
pattern = "phone"
pattern2 = "zawadi"
march = re.search(pattern, text)
print(march)
print(march.span())
print(march.start())
print(march.end())
# if it doesnt find a match it returns None
print(re.search(pattern2, text))

# you can use .findall() to return all instances of a pattern in the text
text1 = "my phone is in my phone"
matches = re.findall('phone', text1)
print(len(matches))
print(matches)

# to return each match object
for match in re.finditer('phone', text1):
    #     returns tuples of the start and end index of each occurence
    print(match.span())
    # to return the exact text that matched
    print(match.group())

# Regular Expressions
# Character identifiers
# The Syntax - backslash character for example \d which is a digit
# \d - A DIGIT for example file_\d\d would look for fileunderscoretwodigits e.g file_25
# \w - ALPHANUMERIC e.g \w-\w\w\w  any alphanumeric character followed by a hyphen and 3 more letters or numbers also includes underscores A-b_1
# \s WHITESPACE - a\sb\sc  letter a whitespace letter b whitespace letter c
# \D NON DIGIT \D\D\D three non-digits e.g ABC
# \W NON ALPHANUMERIC \W\W\WWWWW not a letter or number e.g ^.+=)
# \S NON WHITESPACE \S\S\S\S not a whitespace e.g Yoyo

# EXAMPLE

textone = 'My phone nummber is 408-555-7777'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',textone)
# r raw string tells python that the backslash is not meant to be escaped like you would to avoid quote mark errors
# please search for a pattern that is 3digits hyphen 3 digits hyphen 4-digits
print(phone)
# to print the exact matching text
print(phone.group())

# QUANTIFIERS - Allow you to replicate characters in asimpler way
# + means 'search where this specific pattern Occurs more than once.' \w-\w+  alphanumeric followed by hyphen followed by more than one alphanumeric character Version A-b1_1
# {3} Occurs exactly 3 times \D{3} this specific character appears more than once abc
# {2,4} occurs in the range provided eg \d{2,4} digits occuring between 2 to 4 times
# {3,} Occurs 3 or more times \w{3} any alphanumeric characters appearing more than the number provided
# * Occurs more than 0 times e.g A*B*C* a occurs more than 0 times b occurs more thank 0 times and c occurs more than 0 times e.h AAACCC
# ? Once or none E.g  plurals? does s appear once or none e.g plural

# Quantifier with expressions
phone = re.search(r'\d{3}-\d{3}-\d{4}',textone)
print(phone)
# to print the exact matching text
print(phone.group())

# say you wanted to separate pieces of the pattern you can use the compile method
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,textone)
results.group()
# to rturn the specific parts of the pattern
print(results.group(1))
print(results.group(2))
print(results.group(3))

# ADDITIONAL SYNTAX
# | (pipe) means or e.g
re.search(r'cat|dog','the cat is here')
# . (wildcard) means anything before the characters I am looking for re.findall(r'.at','The cat in the hat sat there') will return 'cat','hat,'sat' insted of at,at,at
re.findall(r'.at','The cat in the hat sat there')
# ^ (caret) means start with
re.findall(r'\d','1 is a number')
# $ means ends with
re.findall(r'\d$','2 is a number 6')
# [] means exclude
phrase = 'there are 3 numbers in 34 inside this 5 sentence'
pattern3 = r'[^\d]+' #this says exclude all digits
print(re.findall(pattern3, phrase))
# good way to remove punctuation
phrase_test = "This is a string! But it has punctuation. How can we remove it"
clean = re.findall(r'[^!.?]+', phrase_test)
print(''.join(clean))