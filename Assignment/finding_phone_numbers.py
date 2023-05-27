#this code is to find out the phone number in a message using RegEx module 're'
import re

text="My phone number is 999-321-8594"
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(text)
print ('Phone number found: ' + mo.group())
