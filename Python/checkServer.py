import requests
import time
#from playsound import playsound


url = 'https://www.google.com/'

while 1:
    try:
        resposta = requests.get(url,timeout=(5,14))
        print(resposta.status_code)
        if resposta.status_code == 200:
            #playsound('done.mp3')
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXX" + reposta.text)
            print("up")
            break
        else:
            print(resposta)
            print("NO RESPONSE")
        print(resposta.status_code)

    except:
        timenow = time.asctime( time.localtime(time.time()))
        #playsound('miss.mp3')
        print(url,"TimeOUT" , timenow)
    else:
        print("Completed RUN")
    time.sleep(10)
