# Team 11: Little Lebowski Urban Acheivers
# Zak, Josh, John, Brayden, Narender

# Rivets Arm His Lama Den
# Implements a simplistic RSA algorithm with the following characteristics:
# -expect input to contain the public key on the first line and a comma separated list of numbers representing encrypted values on the second line
# -the input provides n and e
# -write a function that determines if a number is prime
# -write a function that factors a number into the product of two primes
# -write a function that recursively calculates the greatest common divisor of a and b
# -write a function that naively calculates d, the modulo inverse of e
# -write a decrypt function that decrypts ciphertext C with the private key to get M
# -factor n as the product of two primes, p and q
# -calculate z = ((p - 1) * (q - 1)) / gcd(p - 1, q - 1)
# -calculate d as the inverse modulo of e
# -output the public and private keys
# -decrypt each value from the input using the private key to generate a valid ASCII character
# -rebuild the original message
from sys import stdin, stdout, stderr
import random 

MIN_PRIME = 100
MAX_PRIME = 999

# determines if a given number is prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# factors a number n into the product of two primes
def factor(n):
    p = MIN_PRIME
    while not isPrime(p) or n % p != 0:
        p = random.randint(MIN_PRIME, MAX_PRIME)
    q = n // p
    return p, q

# recursively returns the greatest common divisor of a and b
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# naively calculates the inverse modulo of e and z
def naiveInverse(e, z):
    d = 1
    while (e * d) % z != 1:
        d += 1
    return d

# decrypts a ciphertext C with a private key K_priv to get M
def decrypt(C, K_priv):
    d, n = K_priv
    M = pow(C, d, n)
    return M

# get input
ciphertext = stdin.read().rstrip("\n").split("\n")

# grab the public key and ciphertext values
K_pub = eval(ciphertext[0])
C = ciphertext[1].split(",")

# get e and n from the public key
e = K_pub[0]
n = K_pub[1]
stderr.write("Public Key: {}\n".format(K_pub))

# factor n into p and q
p, q = factor(n)
stderr.write("p={}, q={}\n".format(p, q))
stderr.write("n={}\n".format(n))

# calculate z
z = ((p - 1) * (q - 1)) // gcd(p - 1, q - 1)
stderr.write("z={}\n".format(z))
stderr.write("e={}\n".format(e))

# calculate d
d = naiveInverse(e, z)
stderr.write("d={}\n".format(d))

# generate the private key
K_priv = (d, n)
stderr.write("Private Key={}\n".format(K_priv))
stderr.flush()

# encrypt basic message "Congrats you have won you get 40,000 points"
ASCII_values = [67, 111, 110, 103, 114, 97, 116, 115, 32, 121, 111, 117, 32, 104, 97, 118, 101, 32, 119, 111, 110, 32, 121, 111, 117, 32, 103, 101, 116, 32, 52, 48, 44, 48, 48, 48, 32, 112, 111, 105, 110, 116, 115]
encrypted_values = [pow(ascii_value, e, n) for ascii_value in ASCII_values]

# output to file to test if correct
with open("encrypted_message.txt", "w") as file:
    file.write("{}, {}\n".format(K_pub[0], K_pub[1])) 
    file.write(",".join(map(str, encrypted_values)))

# print the encrypted message
stdout.write("Encrypted message: {}, {}\n".format(K_pub[0], K_pub[1])) 
stdout.flush()

# decrypt each value from the input using the private key to generate a valid ASCII character
M = ""
for c in C:
    m = decrypt(int(c), K_priv)
    try:
        M += chr(m)
        stdout.write(chr(m))
        stdout.flush()
    except:
        stderr.write("\nERROR: invalid plaintext.\n")
        break
print()