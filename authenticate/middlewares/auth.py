import binascii
import json

import jwt

import config
from crypt_manager import getCrypt


def authenticate(func):
    def controller(*args, **kwargs):
        request = args[1]
        authHeader = request.headers['Authorization']
        jwtToken = str.replace(authHeader, 'JWT ', '')
        jwtObj = config.get_jwt()
        decoded = jwt.decode(jwtToken, jwtObj["secret"], jwtObj["alg"])
        crypt = getCrypt()
        encPayload = binascii.unhexlify(decoded['payload'])
        decryptedValue = crypt.decrypt(encPayload)
        payload = json.loads(decryptedValue.decode())
        kwargs['auth'] = payload
        print('auth processed')
        return func(*args, **kwargs)

    return controller
