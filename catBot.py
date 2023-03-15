from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

username = input('Podaj login: ')
password = input('Podaj hasło: ')

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

#Logowanie:
driver = webdriver.Firefox(executable_path=r'C:\Users\kuba3\Documents\visualstudiocode\boty\geckodriver.exe', options=options)
#Po t/ nalezy podać kod z linku prowadzącego do osoby docelowej.
driver.get('https://www.messenger.com/t/100004480355876')

cookies = driver.find_element(By.CLASS_NAME, '_9xo5').click()
time.sleep(2)
user = driver.find_element(By.NAME, 'email').send_keys(username)
password = driver.find_element(By.NAME, 'pass').send_keys(password)
driver.find_element(By.ID, 'loginbutton').click()
time.sleep(5)

#Określanie wiadomosci:
# text = r'Your text message'

#Pobieranie losowego obrazu z internetu:
driver2 = webdriver.Firefox(executable_path=r'C:\Users\kuba3\Documents\catBot\geckodriver.exe', options=options)
driver2.get('https://www.randomkittengenerator.com/')
with open('kitten.png', 'wb') as file:
    img = driver2.find_element(By.CLASS_NAME, 'hot-random-image')
    file.write(img.screenshot_as_png)
driver2.close()

#Wprowadzanie tekstu:
# message = driver.find_element(By.CSS_SELECTOR, 'div.xzsf02u')
# message.click()
# for i in range(len(text)):
#     message.send_keys(text[i])

#Wprowadzanie obrazu:
message = driver.find_element(By.CSS_SELECTOR, 'input.x1s85apg')
photo = os.getcwd()+"\kitten.png"
message.send_keys(photo)

#Wysyłanie wiadomości:
send = driver.find_element(By.CSS_SELECTOR, '.x1emribx')
time.sleep(2)
send.click()
driver.close()
os.remove('kitten.png')





