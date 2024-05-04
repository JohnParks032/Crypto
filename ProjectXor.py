import random

def xor_encrypt(text, key):
    encrypted_text = b""
    # convert to their ASCII values
    key_ascii = [ord(char) for char in key]  
    key_length = len(key_ascii)
    for i, char in enumerate(text):
        key_char = key_ascii[i % key_length]
        # XOR each character with ASCII value
        encrypted_text += bytes([ord(char) ^ key_char])  
    return encrypted_text

def xor_decrypt(encrypted_text, key):
    decrypted_text = ""
    # convert to their ASCII values
    key_ascii = [ord(char) for char in key]  
    key_length = len(key_ascii)
    for i, byte in enumerate(encrypted_text):
        key_char = key_ascii[i % key_length]
        # XOR each character with ASCII value
        decrypted_text += chr(byte ^ key_char)
    return decrypted_text

with open("filetoXor.txt", "r") as file:
    original_text = file.read()

secret_message = "This is a secret message"
secret_message_length = len(secret_message)
# make sure it fits in the random spot i place it
start_point = random.randint(0, len(original_text) - secret_message_length) 
modified_text = original_text[:start_point] + secret_message + original_text[start_point:]

# random to be harder
possible_keys = ["tree", "forest", "woods", "jungle"]

# just get random key
random_index = random.randint(0, len(possible_keys) - 1)
key = possible_keys[random_index]

encrypted_text = xor_encrypt(modified_text, key)

print("Encrypted text:", encrypted_text)

with open("encrypted_text.txt", "wb") as file:  
    file.write(encrypted_text)  

with open("encrypted_text.txt", "rb") as file:  
    encrypted_text = file.read()  

decrypted_text = xor_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

