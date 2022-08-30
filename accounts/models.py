from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profiles/images")

    def __str__(self):
        return self.user.username
