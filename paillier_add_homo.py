#Written and Compiled on Python IDLE 3.7. Code will malfunction for Python 2.x
from phe import paillier
import time
public_key, private_key = paillier.generate_paillier_keypair()
print("\nPaillier Additive Homomorphic Encryptor")
print("\nThe Public Key is(represented in Hexadecimal):")
print(public_key)
print("\nEnter a number:")
x=int(input())
enc_x= public_key.encrypt(x)
print("\nThe Encrypted Number is(represented in Hexadecimal):")
print(hex(enc_x.ciphertext()))
print("\nEnter another number:")
y=int(input())
enc_y= public_key.encrypt(y)
print("\nThe Encrypted Number is(represented in Hexadecimal):")
print(hex(enc_y.ciphertext()))
enc_result= enc_x + enc_y
print("\nThe Encrypted result is(represented in Hexadecimal):")
print(hex(enc_result.ciphertext ()))
print("\nAfter Decryption the result of addition is:" + str(private_key.decrypt(enc_result)))
time.sleep(10)
