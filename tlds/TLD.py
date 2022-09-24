from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd


#added a comment
website = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get(website)
#driver.maximize_window()
element=driver.find_element(By.XPATH, '/html/body/pre')
TLD=element.text
TLD=TLD.split('\n')[1:]
driver.quit()
database=pd.DataFrame(dict(TLDs=TLD))
database.to_csv('TLD.csv')
print(TLD)



