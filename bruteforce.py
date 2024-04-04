import hashlib

words = open('abridged_rockyou.txt', 'r')
rockyou = words.read()

shapass = open('mstoll3-shapass', 'r')
passwd = shapass.readline()
print(passwd)

for string in rockyou:
    print(string)
    hashed = hashlib.sha256(bytes(string, 'utf-8'))
    if(hashed.hexdigest() == passwd):
        print("password is " + string)
        break