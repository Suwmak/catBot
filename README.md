# catBot
A python project for sending random kitten photo to a chosen person by facebook messenger, made to understand and learn basic principles of Selenium WebDriver.

## How does script work?
A script first opens web window and logs into a messenger account with data provided by the user. Nextly opens another web window, from where randomly choose a cat photo and save it in a folder. After this, the script back to the first window and imports previously downloaded image, and send it. In the end, the image is deleted and the tabs are closed.

## How to run:
The whole build was used on Windows 10 and Mozilla browser.\
For running code you must install selenium driver, you can use pip for installation, just type in windows terminal:`` pip install selenium ``\
Additionally you need geckodriver, you can download it from here: https://github.com/mozilla/geckodriver/releases \
Remember to check if path to firefox.exe and geckodriver.exe is correct.\
\
In 'Podaj login: ' bracket you can type email or phone number(if connected).\
In 'Podaj hasło: ' type password to your bot account.\
In 'Podaj URL chatu: ' input whole url to whom you want to send images, e.g.:\
![obraz](https://user-images.githubusercontent.com/127792732/225610806-f6775a1d-0987-43d8-87cc-1a40d0d943e8.png)


## Technologies:
* Python 3.10
* Selenium 4.8
* Geckodriver 0.32
