from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

username = input('Podaj login: ')
password = input('Podaj hasło: ')

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\kuba3\Documents\visualstudiocode\boty\geckodriver.exe', options=options)

#Zapis tego co byłow  schowku
schowek = pyperclip.paste()

#Pobieranie zdjęcia
#driver.get('https://genrandom.com/cats/')
#photo = driver.find_element(By.CLASS_NAME, 'css-14qatfq-stack css-3mf84h')
#photo.send_keys(Keys.CONTROL + Keys.SHIFT + 's')
#photo.click()
#photo.send_keys(Keys.CONTROL + 'c')


#Po t/ nalezy podać kod z linku prowadzącego do osoby docelowej.
driver.get('https://www.messenger.com/t/100002838082080')
#driver.get('https://www.messenger.com/t/5949714175070032')


#Logowanie:
cookies = driver.find_element(By.CLASS_NAME, '_9xo5').click()
user = driver.find_element(By.NAME, 'email').send_keys(username)
password = driver.find_element(By.NAME, 'pass').send_keys(password)
driver.find_element(By.ID, 'loginbutton').click()
time.sleep(5)


#Określanie wiadomosci:
text = r'Dzień dobry'


#Wysyłanie wiadomości:
message = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div')
message.click()
time.sleep(2)
#message.send_keys(Keys.CONTROL+'v')
#dla wysyłania tekstu
for i in range(len(text)):
    message.send_keys(text[i])

#     #dla wysyłania zdjęć
#     message.send_keys(Keys.ENTER)
# pyperclip.copy(schowek)








