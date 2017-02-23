#! /usr/bin/env python3

#Python3 script to open up the google maps of a lcoation from clipboard

import webbrowser, pyperclip
address = pyperclip.paste()
webbrowser.open('https://www.google.ca/maps/place/' + address)

    
