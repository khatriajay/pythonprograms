#! /usr/bin/env python3
# python3 script to copy password for command line arguement to clipboard


# Dictionary of passwords for accounts such as email, facebook and laptop

passwords = {'email':'jkdhksd1323@1',
             'fb':'0934hhg@1111',
             'laptop': '3344'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] 
if account in passwords:                                #If password is found, copy it to clipboard
    pyperclip.copy(passwords[account])
    print('password for ' + account + 'copied to clipbard')
else:
    print('there is no account named ' + account)
