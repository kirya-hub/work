from django.core.exceptions import ValidationError


def validate_text(value):
    if "превосходно" not in value and "раскошно" not in value:
        raise ValidationError()
