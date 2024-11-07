import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if not re.match(r'^[a-zA-Z0-9]{6,}$', value):
        raise ValidationError('ユーザー名は半角英数6文字以上である必要があります。')


def validate_password(value):
    if not re.match(r'^[a-zA-Z0-9]{6,}$', value):
        raise ValidationError('パスワードは半角英数6文字以上である必要があります。')
