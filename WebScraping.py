####login logout linkedin from python####

#to access web driver right here chrome driver
from selenium import webdriver

#to access keys and pass keys in input field
from selenium.webdriver.common.keys import Keys

#import by to access fields correctly
from selenium.webdriver.common.by import By


PATH = "C:\\Users\\User\\Desktop\\WebScraping\\chromedriver.exe"


driver = webdriver.Chrome(PATH)

#access to the browser
driver.get("https://www.linkedin.com/login")

#get title from website
website_title = driver.title

email = ""

password = ""

#search for username element by inspecting the element and get id
search_username = driver.find_element(By.XPATH, "//input[@name='session_key']")

#send keys to the username input
search_username.send_keys(email)



#search for password element by inspecting the element and get id
search_password = driver.find_element(By.XPATH, "//input[@name='session_password']")
#send keys to the password input
search_password.send_keys(password)

search_password.send_keys(Keys.RETURN)

#for logout
driver.get("https://www.linkedin.com/m/logout")



driver.quit()
    