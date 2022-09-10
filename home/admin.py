from django.contrib import admin
from . import models
admin.site.site_header = "Admin Panel"
admin.site.register(models.Message)
