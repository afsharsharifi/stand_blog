from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    father_name = models.CharField(max_length=50, verbose_name="Father Name")
    melicode = models.CharField(max_length=10, verbose_name="Meli Code")
    image = models.ImageField(upload_to="profiles/images", verbose_name="Profile Image")

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username
