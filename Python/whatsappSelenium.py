from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
from glob import glob
import requests
from requests.structures import CaseInsensitiveDict
#import pandas as pd
import random

userData = [{"mess":"test1","number":"919XXXXXXXXX"},
            ]

print("Launching Browser...")


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://web.whatsapp.com/")


while len(driver.find_elements_by_class_name("_2zr6K")) != 0:
    time.sleep(1)



def sendMessage(mess,number,):
    message = "This is a bot generated message:- " + mess
    driver.get("https://web.whatsapp.com/send?phone="+number+"&text="+message)

    while len(driver.find_elements_by_class_name("_1E0Oz")) != 1:
        print("Waiting For Button")
        time.sleep(1)
    print("Got the button...")

    sendJS = "document.getElementsByClassName('_1E0Oz')[0].click()"
    time.sleep(10)
    driver.execute_script(sendJS)
    print("Executing JS")
    if(input("Message Succefully Sent ? Y/N") == "Y"):
        print("Sorry For What just happened .... Please Add This Manually :(")
        print (message)

for user in userData:
    sendMessage(user['mess'],user['number'])
driver.quit()
