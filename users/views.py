import json

import bcrypt, jwt
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from my_settings            import SECRET_KEY, ALGORITHM
from users.models           import User
from core.validations       import (
    validate_email,
    validate_password,
    validate_name,
    validate_contact,
    validate_mbti,
    validate_gender
)

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name     = data['name']
            email    = data['email']
            password = data['password']
            contact  = data['contact']
            mbti     = data.get('mbti', '')
            gender   = data['gender']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE': 'EMAIL_ALREADY_EXIST'}, status=400)

            if User.objects.filter(contact=contact).exists():
                return JsonResponse({'MESSAGE': 'CONTACT_ALREADY_EXIST'}, status=400)

            validate_name(name)
            validate_email(email)
            validate_password(password)
            validate_contact(contact)
            validate_mbti(mbti)
            validate_gender(gender)

            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            user = User(
                email    = email,
                password = hashed_password,
                name     = name,
                contact  = contact,
                mbti     = mbti,
                gender   = gender
            )

            user.full_clean()
            user.save()

            return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'BODY_REQUIRED'}, status=400)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'MESSAGE': e.message}, status=400)


class SigninView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)

            email    = data['email']
            password = data['password']

            validate_email(email)
            validate_password(password)

            encoded_password      = password.encode('utf-8')

            user                  = User.objects.get(email=email)
            encoded_user_password = user.password.encode('utf-8')

            if not bcrypt.checkpw(encoded_password, encoded_user_password):
                return JsonResponse({'MESSAGE': 'INVALID_PASSWORD'}, status=401)

            payload      = {'user_id': user.id}
            access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse(
                {'MESSAGE': 'SUCCESS', 'TOKEN': access_token},
                status=200
            )

        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'BODY_REQUIRED'}, status=400)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'MESSAGE': e.message}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_EMAIL'}, status=401)
