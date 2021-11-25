from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError

def validate_email(email):
    if len(email) > 254:
        raise ValidationError('EMAIL_TOO_LONG')

    EmailValidator(message='INVALID_EMAIL')(email)

def validate_name(name):
    if len(name) < 3:
        raise ValidationError('NAME_TOO_SHORT')
    if len(name) > 15:
        raise ValidationError('NAME_TOO_LONG')

def validate_password(password):
    PASSWORD_REGEX = '''^.*(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,}$'''

    if len(password) < 8:
        raise ValidationError('PASSWORD_TOO_SHORT')
    if len(password) > 45:
        raise ValidationError('PASSWORD_TOO_LONG')

    RegexValidator(regex=PASSWORD_REGEX, message='INVALID_PASSWORD')(password)

def validate_contact(contact):
    CONTACT_REGEX = '''^\+[\d]{1,3}\.[\d]{9,14}$'''

    if len(contact) < 12:
        raise ValidationError('CONTACT_TOO_SHORT')
    if len(contact) > 19:
        raise ValidationError('CONTACT_TOO_LONG')

    RegexValidator(regex=CONTACT_REGEX, message='INVALID_CONTACT')(contact)

def validate_mbti(mbti):
    MBTI_REGEX = '''^[ie][ns][ft][jp]$'''

    if mbti == '':
        return

    RegexValidator(regex=MBTI_REGEX, message='INVALID_MBTI')(mbti)

def validate_gender(gender):
    GENDER_LIST = ['MALE', 'FEMALE', 'UNDEFINED']

    if gender not in GENDER_LIST:
        raise ValidationError('INVALID_GENDER')
