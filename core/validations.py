from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError

PASSWORD_REGEX      = '''^.*(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!"#$%&'()*+,\-./:;<=>?@[＼\]^_`{|}~\\)])[\w!"#$%&'()*+,\-./:;<=>?@[＼\]^`{|}~\\)]{8,}$'''
CONTACT_REGEX       = '''^\+[\d]{1,3}\.[\d]{9,14}$'''
MBTI_REGEX          = '''^[ie][ns][ft][jp]$'''
GENDER_LIST         = ['MALE', 'FEMALE', 'UNDEFINED']

EMAIL_MAX_LENGTH    = 254
NAME_MIN_LENGTH     = 2
NAME_MAX_LENGTH     = 15
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 45
CONTACT_MIN_LENGTH  = 12
CONTACT_MAX_LENGTH  = 19

def validate_email(email):
    if type(email) is not str:
        raise ValidationError('EMAIL_MOST_BE_STR')
    if len(email) > EMAIL_MAX_LENGTH:
        raise ValidationError('EMAIL_TOO_LONG')

    EmailValidator(message='INVALID_EMAIL')(email)

def validate_name(name):
    if type(name) is not str:
        raise ValidationError('NAME_MOST_BE_STR')
    if len(name) < NAME_MIN_LENGTH:
        raise ValidationError('NAME_TOO_SHORT')

    if len(name) > NAME_MAX_LENGTH:
        raise ValidationError('NAME_TOO_LONG')

def validate_password(password):
    if type(password) is not str:
        raise ValidationError('PASSWORD_MOST_BE_STR')

    if len(password) < PASSWORD_MIN_LENGTH:
        raise ValidationError('PASSWORD_TOO_SHORT')

    if len(password) > PASSWORD_MAX_LENGTH:
        raise ValidationError('PASSWORD_TOO_LONG')

    RegexValidator(regex=PASSWORD_REGEX, message='INVALID_PASSWORD')(password)

def validate_contact(contact):
    if type(contact) is not str:
        raise ValidationError('CONTACT_MOST_BE_STR')

    if len(contact) < CONTACT_MIN_LENGTH:
        raise ValidationError('CONTACT_TOO_SHORT')

    if len(contact) > CONTACT_MAX_LENGTH:
        raise ValidationError('CONTACT_TOO_LONG')

    RegexValidator(regex=CONTACT_REGEX, message='INVALID_CONTACT')(contact)

def validate_mbti(mbti):
    if type(MBTI) is not str:
        raise ValidationError('MBTI_MOST_BE_STR')

    if mbti == '':
        return

    RegexValidator(regex=MBTI_REGEX, message='INVALID_MBTI')(mbti)

def validate_gender(gender):
    if type(gender) is not str:
        raise ValidationError('GENDER_MOST_BE_STR')

    if gender not in GENDER_LIST:
        raise ValidationError('INVALID_GENDER')
