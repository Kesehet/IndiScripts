import requests

arquivo = open('directory-list-2.3-medium.txt')

linhas = arquivo.readlines()

url = 'http://192.168.1.1/'
endslash = '/'

for linha in linhas:
    codigo = 404
    if linha[0] != "#":
        linha = linha.replace("\n","/")
        complete = url+linha
        
        resposta = requests.get(complete)
        
        if resposta.status_code == 200:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXX")
            print(complete)
        else:
            print(resposta)
    
        
