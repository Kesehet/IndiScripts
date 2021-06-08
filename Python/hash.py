from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Yay! Successfully mined bitcoins with nonce value:"+str(nonce))
            generateEntry(block_number,transactions,prefix_zeros,previous_hash,nonce,new_hash)
            return new_hash

    raise BaseException("Couldn't find correct has after trying "+str(MAX_NONCE)+" times")

def generateEntry(bln,tr,diff,prehash,nonce,hash):
  f = open("hash.csv", "a")
  strToWrite =   "\n"+str(bln)+","+tr+","+str(diff)+","+prehash+","+str(nonce)+commaSeperate(hash)
  f.write(strToWrite)
  f.close()
def commaSeperate(text):
  ret = ""
  for i in range(len(text)):
    ret = ret+","+text[i]
  return ret

def specific_string(length):  
    sample_string = 'abcdefghijklmnopqrstuvwxyz' # define the specific string  
    # define the condition for random string  
    return ''.join((random.choice(sample_string)) for x in range(length))  
     

import random
import time

if __name__=='__main__':
  # hashColl = ""
  # for y in range(64):
  #   hashColl = hashColl+",h"+str(y)
  # fa = open("hash.csv", "w")
  # header = "Block_Number,Transactions,Difficulty,Previous_Hash,Nonce"+hashColl
  # print(header)
  # fa.write(header)
  # fa.close()
  oldhash = '0004fa0908d73687f2a55ff820b840dfd4e384952bc8d2103791550b4439a2b1'
  initTime = time.time()
  for i in range(1000):
    transactions= specific_string(10)
    difficulty=random.randint(1,6) # try changing this to higher number and you will see it will take more time for mining as difficulty increases

    startBlock = time.time()
    print("start mining for string " + transactions +"at difficulty "+str(difficulty) )
    new_hash = mine(i,transactions,oldhash, difficulty)
    total_time = (time.time() - startBlock)  
    print("_______BLOCKS LEFT "+str(1000-i)+"____________" )
    print("end mining. Mining took: "+str(total_time)+" seconds at Difficulty :-" + str(difficulty))
    print(new_hash)
    oldhash = new_hash
    print("")
  print(str((time.time() - initTime)))