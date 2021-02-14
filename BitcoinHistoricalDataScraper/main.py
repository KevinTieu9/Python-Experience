# Kevin Tieu
# CS 232 Python
# Spring 2021
# Project 1 - Scripting Project - Webscraping

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #make selenium move to an element in view for this situation
import requests
import time #for timing some button presses
import csv  #for importing data into a CSV file



# This will be where the web scraping will be at.
# This will scrape different crytocurrencies attached to it
# to look for highs, lows, the date, and possibly a few variables


#Used to locate and start the chrome web driver
driver = webdriver.Chrome(executable_path = r'C:\Users\Kevin\Desktop\HSU\Spring2021\CS232\p01-kt216\chromedriver.exe')
#Used to get to the url in question
driver.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')


#This part is to exit the Cookie notification that properly blocks the program from getting more data
driver.implicitly_wait(2)
element = driver.find_element_by_xpath('//*[@id="cmc-cookie-policy-banner"]/div[2]').click()

#webdriver scrolls towards the web element that contains the button
#so that it can be clicked on to add more data


element = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div/div[1]/span/button')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()

bc = 1

element = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/button[1]')
for buttonClick in range(1, 93):
        print(bc)
        #time.sleep(1)
        #element = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/p[1]')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.click()
        buttonClick = buttonClick + 1
        bc = bc +1

element = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[5]/div[2]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()


element = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/button[2]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()

time.sleep(5)

# creates the titles/fields for where the data will be under.
fields = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']

# name of csv file  
filename = "Project2.csv"

with open(filename, 'a', newline='') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)
    
    # collecting 7 types of data, for ~365 days
    # while loop until 367 days, about a year of data.
    for daycount in range(2, 2846):
    
    # String concatenation is used to peice together the xpath number variables.
     
        rows = [ [driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[1]").text,
                  driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[2]").text,
                  driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[3]").text,
                  driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[4]").text,
                  driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[5]").text,
                  driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[6]").text,
                  driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[' + str(daycount) + "]" + "/td" + "[7]").text]]
        
    # writing the data rows  
        csvwriter.writerows(rows)  

        daycount = daycount + 1

#shut down webdriver. 
driver.quit()



# If time permits, this is where the uploading to Oracle database will be at.
