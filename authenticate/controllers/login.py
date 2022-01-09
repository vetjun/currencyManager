import binascii
import json
import jwt
import config

from django.http import JsonResponse

from authenticate.middlewares.auth import authenticate
from crypt_manager import getCrypt


class Login:
    @classmethod
    def login(cls, request):
        try:
            bodyJson = json.loads(request.body)
            username = bodyJson['username']
            password = bodyJson['password']
        except Exception as exception:
            return JsonResponse({'success': False, 'message': exception})
        jwtObj = config.get_jwt()
        crypt = getCrypt()
        encPayload = crypt.encrypt(json.dumps({"username": username, "password": password}))
        jwt_token = jwt.encode({"payload": binascii.hexlify(encPayload).decode()}, jwtObj["secret"], algorithm=jwtObj["alg"])
        return JsonResponse({'success': True, 'token': jwt_token})

    @classmethod
    @authenticate
    def me(cls, request, auth=None):
        return JsonResponse({'auth': auth})