# catBot
A python project for sending random kitten photo to a chosen person by facebook messenger, made to understand and learn basic principles of Selenium WebDriver.

## How does script work?
A script first opens web window and logs into a messenger account with data provided by the user. Nextly opens another web window, from where randomly choose a cat photo and save it in a folder. After this, the script back to the first window and imports previously downloaded image, and send it. In the end, the image is deleted and the tabs are closed.

## Technologies:
* Python 3.10
* Selenium 4.8
* Geckodriver 0.32
