from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd


#added a comment
website = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(website)
driver.maximize_window()
element=driver.find_element(By.XPATH, '/html/body/pre')
TLD=element.text
TLD=TLD.split('\n')[1:]
driver.quit()
database=pd.DataFrame(dict(TLDs=TLD))
database.to_csv('C:\\Users\\OmiIn\\PycharmProjects\\pythonProject\\TLD.csv')
print(TLD)



