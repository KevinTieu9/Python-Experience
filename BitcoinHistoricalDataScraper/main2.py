# Kevin Tieu
# CS 232 Python
# Spring 2021
# Project 1 - Scripting Project - Webscraping

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #make selenium move to an element in view for this situation
import requests
import bs4
import time #for timing some button presses
import xlwt #to excel data

dateList=[]
openlist=[]
highlist=[]
lowList=[]
closeList=[]
volumeList=[]
capList=[]

# This will be where the web scraping will be at.
# This will scrape different crytocurrencies attached to it
# to look for highs, lows, the date, and possibly a few variables
# once I can get it to work properly.


#Used to locate and start the chrome web driver
driver = webdriver.Chrome(executable_path = r'C:\Users\Kevin\Desktop\HSU\Spring2021\CS232\p01-kt216\chromedriver.exe')
#Used to get to the url in question
driver.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')


#This part is to exit the Cookie notification that properly blocks the program from getting more data
driver.implicitly_wait(1)
element = driver.find_element_by_xpath('//*[@id="cmc-cookie-policy-banner"]/div[2]').click()

#webdriver scrolls towards the web element that contains the button
#so that it can be clicked on to add more data
for buttonClick in range(1, 15):
        element = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/p[1]')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.click()
        buttonClick = buttonClick + 1

# collecting 7 types of data, for ~365 days

daycount = 2
while (daycount <=367):
    count = 1

    # last_height = driver.execute_script("return document.body.scrollHeight")
    
    # While loop to collect all the data within a certain day
    # String concatenation is used to peice together the xpath number variables.

    
    while (count <=7):
        print(driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[" + str(count) + "]").text)
        count = count + 1
    daycount = daycount + 1






















    #driver.findElement(By.linkText("Login")).click()
   # //*[@id="__next"]/div/div[2]/div/div[3]/div/div/p[1]/button

#//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[3]/td[1]


# Here shall be where the importing of data to excel/.csv should be



# If time permits, this is where the uploading to Oracle database will be at.

#r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
#soup = bs4.BeautifulSoup(r.text,'lxml')

#tr = soup.find_all('td',{'class':'text-left'})
#for item in tr[:10]:
    #print(item.find('td',{'class':'text-right'}).text)
