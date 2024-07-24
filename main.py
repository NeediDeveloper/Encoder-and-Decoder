import random
import string
msg = input("Enter Message : ")
words = msg.split(" ")
coding = int(input("Enter 1 for Encode and 0 for Decode : "))
# This is one line if else statement 
coding == True if coding == 1 else False
# This is our Encoder
if coding:
    new_msg = []
    for word in words:
        if len(word)>=3:
            ran_dom1 = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=4))
            ran_dom2 = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=4))
            secret_msg = ran_dom1 + word[2:] + word[:2] + ran_dom2
            new_msg.append(secret_msg)
        else:
            new_msg.append(word[::-1])
    print(" ".join(new_msg))
# This is our Decoder
else:
    new_msg = []
    for word in words:
        if len(word)>=3:
            secret_msg = word[4:-4]
            secret_msg =secret_msg[-2:] + secret_msg[:-2]
            new_msg.append(secret_msg)
        else:
            new_msg.append(word[::-1])
    print(" ".join(new_msg))
