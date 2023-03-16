from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
import time

def main():
    username = input('Podaj login: ')
    password = input('Podaj hasło: ')
    chat_url = input('Podaj URL chatu: ')
    fb_driver = login(username, password, chat_url)
    send_message(fb_driver)

#Logowanie:
def login(username, password, url):
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=r'C:\Users\kuba3\Documents\catBot\geckodriver.exe', options=options)
    #Po t/ nalezy podać kod z linku prowadzącego do osoby docelowej.
    driver.get(url)
    #cookies
    driver.find_element(By.CLASS_NAME, '_9xo5').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'email').send_keys(username)
    driver.find_element(By.NAME, 'pass').send_keys(password)
    driver.find_element(By.ID, 'loginbutton').click()
    return driver

#Pobieranie losowego obrazu z internetu:
def get_image():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    img_driver = webdriver.Firefox(executable_path=r'C:\Users\kuba3\Documents\catBot\geckodriver.exe', options=options)
    img_driver.get('https://www.randomkittengenerator.com/')
    with open('kitten.png', 'wb') as file:
        img = img_driver.find_element(By.CLASS_NAME, 'hot-random-image')
        file.write(img.screenshot_as_png)
    img_driver.close()

def send_message(driver):
    #Wprowadzanie obrazu:
    get_image()
    message = driver.find_element(By.CSS_SELECTOR, 'input.x1s85apg')
    photo = (Path.cwd() / 'kitten.png')
    message.send_keys(str(photo))
    time.sleep(2)
    Path.unlink(photo)
    #Wprowadzanie tekstu:
    # time.sleep(5)
    # text = 'test'
    # message = driver.find_element(By.CLASS_NAME, 'notranslate')
    # message.click()
    # for i in range(len(text)):
    #     message.send_keys(text[i])
    #Wysyłanie wiadomości:
    send = driver.find_element(By.CSS_SELECTOR, '.x1emribx')
    send.click()
    driver.close()

if __name__ == '__main__':
    main()