#!/usr/local/bin/python3
import sys 

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def alphalookup(letter):

    if ord(letter) <= 90 and ord(letter) >= 65:
        for i in range(0,len(ALPHABET)):
            if ALPHABET[i] == letter:
                return i
            
    elif ord(letter) <= 122 and ord(letter) >= 97:
        for i in range(0,len(alphabet)):
            if alphabet[i] == letter:
                return i
    else:
        pass

        
def encrypt(message,key):
    finalmessage = []
    for i in range(0,len(message)):
        
        if message[i] == " ":
            finalmessage.append(" ")
        
        elif message[i] == "^":
            finalmessage.append("^")
        
        elif ord(message[i]) <= 90 and ord(message[i]) >= 65:
            finalmessage.append(ALPHABET[(alphalookup(message[i])+alphalookup(key[i%len(key)]))%len(ALPHABET)])
        
        elif ord(message[i]) <= 122 and ord(message[i]) >= 67:
            finalmessage.append(alphabet[((26+alphalookup(message[i]))+alphalookup(key[i%len(key)]))%len(alphabet)])

        else: 
            finalmessage.append(message[i])

    encodedmessage = "".join(finalmessage)
    return encodedmessage

def decrypt(message,key):
    finalmessage = []
    for i in range(0,len(message)):
        if message[i] == " ":
            finalmessage.append(" ")
        
        elif message[i] == "^":
            finalmessage.append("^")

        elif ord(message[i]) <= 90 and ord(message[i]) >= 65:
            finalmessage.append(ALPHABET[(alphalookup(message[i])-alphalookup(key[i%len(key)]))%len(ALPHABET)])

        elif ord(message[i]) <= 122 and ord(message[i]) >= 67:
            finalmessage.append(alphabet[((26+alphalookup(message[i]))-alphalookup(key[i%len(key)]))%len(alphabet)])

        else:
            finalmessage.append(message[i])

    decodedmessage = "".join(finalmessage)
    return decodedmessage
    
def main():
    x = "D"
    if len(sys.argv) != 3:
        print("invalid number of arguments")
        return 
    elif sys.argv[1] != "-e" and sys.argv[1] != "-d":
        print("invalid argument")
        return
    
    elif sys.argv[1] == "-e":
        try:
            while True:
                key = sys.argv[2]
                message = input()
                print(encrypt(message,key))
        except EOFError:
            print("^D")
            
    
    elif sys.argv[1] == "-d":
        try:
            while True:
                key = sys.argv[2]  
                message = input()
                print(decrypt(message,key))
        except EOFError:
            print("^D")
main()