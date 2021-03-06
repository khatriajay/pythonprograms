#! /usr/bin/env python3
#Python3 script to grab phone number and email address from a text on website. 

#phone number regex

import pyperclip, re
phonenum= re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)


#email regex

email= re.compile(r'''(
    [a-zA-Z0-9._%+-]+         
    @
    [a-zA-Z0-9.-]+          
    (\.[a-zA-Z]{2,4})       
    )''', re.VERBOSE)

#find a match

message= str(pyperclip.paste())
matches= []
for groups in phonenum.findall(message):
    num= '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        num += ' x' + groups [8]
    matches.append(num)
for groups in email.findall(message):
    matches.append(groups[0])


# copy results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print ('No phone numbers or email address were found')
