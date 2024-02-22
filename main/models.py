from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# def validate_py_file(value):
#     if not value.name.endswith('.py'):
#         raise ValidationError('Only .py files are allowed.')


CHOICES = [
    ('middle', "Middle"),
    ('final', "Final")
]


class ContactModel(models.Model):
    full_name = models.CharField(max_length=100)
    group_name = models.CharField(max_length=20)
    radio = models.CharField(max_length=20, choices=CHOICES, blank=True, null=True)
    file = models.FileField(upload_to='files/',
                            # validators=[FileExtensionValidator(allowed_extensions=['py']), validate_py_file]
                            )

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
