import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart # makes texting your phone through email happen
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #make selenium move to an element in view for this situation
import requests
import time #for timing some button presses


#Used to locate and start the chrome web driver
driver = webdriver.Chrome(executable_path = r'Add the path of your webdriver here')
#Change it from chrome or to the other webdrivers (like firefox) if you aren't using chrome

#Used to get to the url in question, since this is for a Crytopcurrency site, this link will lead us to Binance
#If you want, you can have multiple webdrivers open, in this case, it is only one
driver.get('https://accounts.binance.us/en/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS51cy9lbi9ob21l')

#wait for site to load.
time.sleep(5)

#Username and Password of the site
naming = "type your email here you used for the site"
bipas = "type your password here"

#these three parts will click and input information udner username, password, and click login.

element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/form/div[1]/div[1]/div/div/div/input')
element.click()
element.send_keys(naming)

element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/form/div[1]/div[2]/div/div/div/input')
element.click()
element.send_keys(bipas)


element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/form/button')
element.click()


#This part you will need to manually do because of bot detection, you can lower this if you are fast
#60 seconds is a lot of time
time.sleep(60)


#Depending on what kind of cryptocurrency you are watching, add the link to the one that has the ticker information
driver.get('https://www.binance.us/en/trade/ADA_USD')


#this part will have an infinite loop unless, KeyboardInterrupt is detected (default is CTRL + C)
try:
    while True:

        #While stock is less than .9600, change x to stock price
        #This will constantly compare x to a predefined number until it is greater than it
        #If X is still less than .9600, it will make x = to that lesser number
        x = float(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]').text)
        while x < 0.9600:
            x = float(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]').text)

        #Print X so that you can view it, this can be commented out.
            print(x)

        #Once it reachs .9600, limit sell is reached and it sells
            
        #I put a limit buy for .9250 on this section
        #it will click on the text portion to input the price
        #how many shares (in this case, I put 100% of the money I can afford to put in)
        # and click send to wait)
        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[2]/div/input')
        element.click()
        element.send_keys('.9250')


        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[4]/div/input[4]')
        element.click()

        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[7]/div/button')
        element.click()

        #Once it figures out that my Limit Buy goes through because price went below .9250
        #It does a ticker check just like when I was selling for .9600
        
        while x > 0.9250:
            x = float(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]').text)
            print(x)

        #The program goes back to putting a limit Sell for .9600
        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/form/div[2]/div/input')
        element.click()
        element.send_keys('.9600')


        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/input[4]')
        element.click()

        element = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/form/div[7]/div/button')
        element.click()
        


        email = "YourEmail@location.com"
        pas = "YourEmailPassword"

        sms_gateway = 'xxxXXXxxxx@carrier.com' #X refers to your number, carrier refers to your carrier
        # The server we use to send emails in our case it will be hotmail/outlook but every email provider has a different smtp 
        # and port is also provided by the email provider.
        smtp = "smtp.live.com"
        #port is different for every email provider, look it up!
        port = 587
        # This will start our email server
        server = smtplib.SMTP(smtp,port)
        # Starting the server
        server.starttls()
        # Now we need to login
        server.login(email,pas)

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = sms_gateway
        # Make sure you add a new line in the subject
        msg['Subject'] = "Email Subject goes here\n"
        # Make sure you also add new lines to your body
        body = "Everything else you want to talk about is put here\n"
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))

        sms = msg.as_string()

        server.sendmail(email,sms_gateway,sms)

        #quit the server
        server.quit()

        #Return back to the top of while loop unless your Keyboard Interrupt
except KeyboardInterrupt:
    pass
