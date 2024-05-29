from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver = webdriver.Chrome()
# Code to query the webpage of the security lab
webpage = requests.get("https://security.scs.carleton.ca/people.html")
soup = BeautifulSoup(webpage.text)


# Code to find all the names of the students and lecturers in the lab 
h7_objects = soup.find_all("h7")
for i in h7_objects:
    #Code to switch to a new browser tab 
    driver.switch_to.new_window('tab')
    #Code to search for graduate students on google search engine
    driver.get("https://www.google.com/search?q="+(i.b.string + " AND Linkedin AND Carleton University"))

