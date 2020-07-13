import os
import time
from threading import Thread

import requests
from bs4 import BeautifulSoup


class logger:
        
        #Delete this if it isnt being used
        def __init__(self):
                self.string = '[{}]\033[3{}m {}\033[0m'
                os.environ['NY'] = 'EST+05EDT,M4.1.0,M10.5.0'
                time.tzset()



def viewEbaySite (url):
    running = False
    if(running == False): #Runs once
        response = session.get(url)  
        if (response.status_code == 200):
            print('\033[92m' + "View: Successful!") #Prints Green
        else:
            print('\033[91m' + "View: Unsuccessful") #Prints Red
        running = True              
        

        

session = requests.session()
url = str(raw_input('\033[95m' + "What is the url of the item? :"))
viewsAmount = input('\033[94m' + "How many views would you like (I reccommend 100 at a time) :")

def addViews () :
    viewCounter = -30
    while (viewCounter < viewsAmount):
        t = Thread(target = lambda: viewEbaySite(url))
        t.start()
        viewCounter = viewCounter + 1
    
       
    
        
#MAIN

addViews()


#time.sleep(1)


        


    
   



