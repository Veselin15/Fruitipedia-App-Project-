import re

from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not bool(re.fullmatch(r"[A-Za-z ]+", value)):
        raise ValidationError("Fruit name should contain only letters and whitespaces!")