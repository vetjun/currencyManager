from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class CryptManager:
    def __init__(self):
        encKey = RSA.import_key(open("keys/receiver.pem").read())
        dencKey = RSA.import_key(open("keys/private.pem").read())
        self.cipher_enc = PKCS1_OAEP.new(encKey)
        self.cipher_denc = PKCS1_OAEP.new(dencKey)

    def encrypt(self, value):
        return self.cipher_enc.encrypt(str.encode(value))

    def decrypt(self, value):
        return self.cipher_denc.decrypt(value)


crypt = CryptManager()


def getCrypt():
    return crypt

