from django.db import models
from django.core import validators

import uuid

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4().hex[:16], ext.lower())
    return 'testuser/{sub}/{filename}'.format(
        sub=filename[:2],
        filename=filename,
    )



class TestUser(models.Model):
    email = models.EmailField()
    password = models.CharField(
        max_length=16,
        validators=[
            validators.MaxLengthValidator(16),
            validators.MinLengthValidator(3)
        ]
    )
    join_date = models.DateField(auto_now_add=True)
    username = models.CharField(
        max_length=16,
        validators=[
            validators.MaxLengthValidator(16),
            validators.MinLengthValidator(8)
        ]
    )
    is_active = models.BooleanField(default=False)
    company = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    avatar = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True
    )


    def __str__(self):
        return self.username