####login logout linkedin from python####

#to access web driver right here chrome driver
from selenium import webdriver

#to access keys and pass keys in input field
from selenium.webdriver.common.keys import Keys

#import by to access fields correctly
from selenium.webdriver.common.by import By

import time

PATH = "C:\\Users\\User\\Desktop\\WebScraping\\chromedriver.exe"


driver = webdriver.Chrome(PATH)



#get title from website
website_title = driver.title


#set email and password as parameters
email = ""

password = ""


def login(email, password):
    
    #access to the browser
    driver.get("https://www.linkedin.com/login")

    #search for username element by inspecting the element and get id
    search_username = driver.find_element(By.XPATH, "//input[@name='session_key']")
    
    #send keys to the username input
    search_username.send_keys(email)
    
    #search for password element by inspecting the element and get id
    search_password = driver.find_element(By.XPATH, "//input[@name='session_password']")
    #send keys to the password input
    search_password.send_keys(password)
    
    search_password.send_keys(Keys.RETURN)

def logout():
    #for logout
    driver.get("https://www.linkedin.com/m/logout")


#to call functions login logout after set email & password

#to login call of function : comment out this line below by removing #
#login(email,password)

#to logout call of function : comment out this line below by removing #
#logout()


#function that extract jobs by keywords as parameter
def extract_jobs_by_keywords(name):
    driver.get("https://www.linkedin.com/jobs")
    search_keywords = driver.find_element(By.XPATH, "//input[@name='keywords']")
    search_keywords.send_keys(name)
    search_keywords.send_keys(Keys.RETURN)

#to get jobs by keywords call of function : comment out this line below by removing #
#extract_jobs_by_keywords("data scientist")

#function that extract jobs by location as parameter

def extract_jobs_by_country(country):
    driver.get("https://www.linkedin.com/jobs")
    search_by_location = driver.find_element(By.XPATH, "//input[@name='location']")
    search_by_location.send_keys(country)
    search_by_location.send_keys(Keys.RETURN)

#to get jobs by country call of function : comment out this line below by removing #
#extract_jobs_by_country("canada")

#time sleep to let the service available for 1 min
time.sleep(60)

driver.quit()
