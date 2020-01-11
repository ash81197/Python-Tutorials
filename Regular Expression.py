'''
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
\b the whitespaces around words
\. a period
.  any character, except for a newline

Modifiers:
{1,3} we're expecting 1-3
+ match 1 or more
? match 0 or 1
* match 0 or more
$ match the end of the string
^ match the beginning of the string
| either or
[] range or "variance" [1-5a-qA-Z]
{x} expecting "x" amount

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Things that need to be escaped:
. + * ? [ ] { } $ ^ ( ) | \
'''

import re
exampleString = '''
Jessica is 15 years old,  and Daniel is 27 years old.
Edward is 57 years old, and his father, Oscar, is 102.
'''
#ages = re.findall(r'\d{1-3}', exampleString)
ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)
print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)
