import json

import bcrypt
from django.views import View
from django.http  import JsonResponse

from users.models import User

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name = data['name']
            email = data['email']
            password = data['password']
            contact = data['contact']
            mbti = data.get('mbti', None)
            gender = data['gender']

            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            user = User()

            return JsonResponse({'MESSAGE': 'CREATED'}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
