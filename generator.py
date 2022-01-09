from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import config

'''secret_code = config.get_security()['enc_secret']
key = RSA.generate(4096)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                               protection="scryptAndAES128-CBC")

file_out = open("keys/rsa_key", "wb")
file_out.write(encrypted_key)
file_out.close()

print(key.publickey().export_key())'''

'''secret_code = config.get_security()['enc_secret']
encoded_key = open("keys/rsa_key", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)

print(key.publickey().export_key())'''

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("keys/private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("keys/receiver.pem", "wb")
file_out.write(public_key)
file_out.close()
