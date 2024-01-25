#! /usr/bin/env python3

#Python script to fetch weekly weather forecast for major cities in British Columbia, Canada. 

import bs4, requests

#Store the city code for URL fetch as a dictionary.

citycode= {'Vancouver': 74, 'Victoria': 85, 'White Rock': 62, 'Abbotsford': 81, 'Port Hardy': 89, 'Chilliwack': 24, 'Nanaimo': 20, 'Tofino': 17, 'Vernon': 35, 'Courtenay': 92, 'Sechelt': 3, 'Kamloops': 45, 'Golden': 34, 'Prince George': 79, 'Kelowna': 48, 'Lillooet': 28, 'Terrace': 80, 'Nelson': 37, 'Squamish': 50, 'Whistler': 86}


while True:

    print('Enter a city name (Press \'e\' and hit Enter to exit): ')
    name=input()
    
#If city name exists in dictionary defined above, do this.
    
    if name in citycode:
        url = 'https://weather.gc.ca/city/pages/' + 'bc-' + str(citycode[name]) + '_metric_e.html'
        a=requests.get(url)
        a.raise_for_status()
        b=bs4.BeautifulSoup(a.content, 'html.parser')

#Find all h2 tags from website and then get text value of h2[5] which stores weather alert text. 
        
        alert=b.find_all('h2')[5].get_text()                                   

        # Find the type of alert and print the complete information
        
        if alert =='\nSNOWFALL WARNING IN EFFECT\n':
            link= b.find_all('a', href=True, text='SNOWFALL WARNING IN EFFECT')
            for links in link:
                l= links['href']
            url2='https://weather.gc.ca' + str(l)
            c=requests.get(url2)
            c.raise_for_status()
            d=bs4.BeautifulSoup(c.content, 'html.parser')
            statement=d.find_all('p')[1].get_text()
            print(statement)
        elif alert== '\nSPECIAL WEATHER STATEMENT IN EFFECT\n':
            link= b.find_all('a', href=True, text='SPECIAL WEATHER STATEMENT IN EFFECT')
            for links in link:
                l= links['href']
            url2='https://weather.gc.ca' + str(l)
            c=requests.get(url2)
            c.raise_for_status()
            d=bs4.BeautifulSoup(c.content, 'html.parser')
            statement=d.find_all('p')[1].get_text()
            print(statement)
        else:
            print(alert)

#Find minimum and maximum temperature divs and store them in 2 different variables
        
        minimum=b.find_all('span', class_='low wxo-metric-hide')
        maximum=b.find_all('span', class_='high wxo-metric-hide')

#Delete the repetitive data
        
        del maximum[6:12]
        del minimum[6]

#Print the temperature forecasts
        
        print ('\nMinimum temperature for tonight is: ' + minimum[0].get_text())
        print('Max temperature for next 6 days: \n' + maximum[0].get_text() + maximum[1].get_text() + maximum[2].get_text() + maximum[3].get_text() + maximum[4].get_text() + maximum[5].get_text())
        print ('Minimum temperature for next 5 days: \n' + minimum[1].get_text() + minimum[2].get_text() + minimum[3].get_text() + minimum[4].get_text() + minimum[5].get_text())

#For blank city name, continue.
        
    elif name == '':
        continue
    
#Condition to exit the program
    
    elif name == 'e':
        break
    
#If the name of city does not exist in the dictionary value
    
    else:
        print('No info for this city.\n')
        
        
    

        
        
        

        
                
