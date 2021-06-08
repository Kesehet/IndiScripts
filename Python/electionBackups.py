import requests
import os
import json
import time
import pandas as pd
    
    
    
def resetMainUnVerifyfile(fi):
    
    maindf = pd.read_csv('mainUnVerify.csv')
    g = open(fi,"r")
    y = g.read()
    g.close()
    
    list2 = []
    for i in y.split("&&&"):
        ls = i.split(",")
        if ls[0].strip() == "":
            continue
        list2.append(ls)
    newdf = pd.DataFrame(list2, columns = ['Name', 'Pass','Pin'])
    z=newdf

    maindf = maindf.applymap(str)
    newdf = newdf.applymap(str)
    
    z = pd.merge(maindf,newdf, how='outer')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
        
        z.to_csv("mainUnVerify.csv" , index=False)

    
    
def resetMainVerifyfile(fi):
    
    maindf = pd.read_csv('mainVerify.csv')
    g = open(fi,"r")
    y = g.read()
    g.close()
    
    list2 = []
    for i in y.split("&&&"):
        ls = i.split(",")
        if ls[0].strip() == "":
            continue
        list2.append( ls)
    newdf = pd.DataFrame(list2, columns = ['Name', 'Pass'])    
    z = newdf
    maindf = maindf.applymap(str)
    newdf = newdf.applymap(str)
    z = pd.merge(maindf,newdf, how='outer')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
        
        
        z.to_csv("mainVerify.csv" , index=False)



def userCount(s):
    return len(s.split("&&&")) -1

while True:
    url = "https://evpbtts.kesehetzayyan.repl.co/failProof/"


    resp = requests.get(url)

    jso = json.loads(resp.text)


    try:
        os.mkdir("backups")
        os.mkdir("backups/unverified")
        os.mkdir("backups/verified")
        os.mkdir("backups/votes")
    except:
        pass
    current_time = time.localtime()
    tm = time.strftime('%a, %d %b %Y %H-%M-%S GMT', current_time)
    print("Unverified",userCount(jso['unverified']),"|", "Verified" , userCount(jso['verified']),"|", "Votes" , userCount(jso['votes']) )
    
    f = open('backups/unverified/'+str(tm)+".txt",'w')
    f.write(jso['unverified'])
    f.close()

    f = open('backups/verified/'+str(tm)+".txt",'w')
    f.write(jso['verified'])
    f.close()

    f = open('backups/votes/'+str(tm)+".txt",'w')
    f.write(jso['votes'])
    f.close()
    df = pd.read_csv('mainVerify.csv')
    df2 = pd.read_csv('mainUnVerify.csv')
    print("Verify ",df[df.columns[0]].count()," | Unverify ",df2[df2.columns[0]].count())

    for file in os.listdir("backups/verified/"):
        if file.endswith(".txt"):
            resetMainVerifyfile(os.path.join("backups/verified/", file))
    for file in os.listdir("backups/unverified/"):
        if file.endswith(".txt"):
            resetMainUnVerifyfile(os.path.join("backups/unverified/", file))
    time.sleep(60*5)
