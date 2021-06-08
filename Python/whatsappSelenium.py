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
import string


def pinGen():
  return ''.join(random.SystemRandom().choice(string.digits) for _ in range(12))

def processValue(p):
    p = str(p)
    p = p.replace('/','')
    p = p.replace('-','')
    p = p.replace(' ','')
    p = p.strip()
    return p

userData = [{"enroll":"test1","pin":pinGen(),"number":"9540867732"},
            {"enroll":"test2","pin":pinGen(),"number":"8826270631"},
            {"enroll":"test4","pin":pinGen(),"number":"9999949511"}
            ]

print("Launching Browser...")


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://web.whatsapp.com/")


while len(driver.find_elements_by_class_name("_2zr6K")) != 0:
    time.sleep(1)



def sendMessage(enrollno,pin,number,):
    message = "This is a bot generated message:-  Your Username is :-"+enrollno + " Your Security Verification code is:- " + pin
    driver.get("https://web.whatsapp.com/send?phone=91"+number+"&text="+message)

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
        addList(enrollno,pin,pinGen())
        




def addList(user,pin,password):
    m = processValue(user)
    url = "https://evpbtts.kesehetzayyan.repl.co/createuser"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"user":"'+m+'","pin":"'+pin+'","passw":"'+password+'"}'
    resp = requests.post(url, headers=headers, data=data)
    print(data)
    print(resp.text)


for user in userData:
    sendMessage(user['enroll'],user['pin'],user['number'])
driver.quit()
