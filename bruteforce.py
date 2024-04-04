import hashlib

words = open('abridged_rockyou.txt', 'r')
rockyou = words.readlines()
for i in range(len(rockyou)):
  rockyou[i] = rockyou[i].strip('\n')

shapass = open('mstoll3-shapass', 'r')
passwd = shapass.readline()
#print(passwd)

writer = open("output.txt", "w")

for string in rockyou:
    #print(string)
    hashed = hashlib.sha256(bytes(string, 'utf-8'))
    #print(hashed.hexdigest())
    writer.write(hashed.hexdigest() + "\n")
    if(hashed.hexdigest() == passwd):
        print("password is " + string)
        break
writer.close()
