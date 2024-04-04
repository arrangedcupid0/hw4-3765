import hashlib

words = open('abridged_rockyou.txt', 'r')
rockyou = words.readlines()
for i in range(len(rockyou)):
  rockyou[i] = rockyou[i].strip('\n')

shapass = open('mstoll3-shapass', 'r')
passwd = shapass.readline()
#print(passwd)

#writer = open("output.txt", "w")
ah = "fuck"
if(str("fuck") == str(ah)):
   print("works in theory")

for string in rockyou:
    #print(string)
    hashed = hashlib.sha256(bytes(string, 'utf-8'))
    hexed = hashed.hexdigest()
    #print(hashed.hexdigest())
    #writer.write(hashed.hexdigest() + "\n")
    #print(str(hexed) + " vs " + str(passwd))
    if(str(hexed) == str(passwd)):
        print("password is " + string)
        break
#writer.close()
