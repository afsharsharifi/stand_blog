from django.db import models

# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    text = models.TextField(verbose_name="Message")
    email = models.EmailField(verbose_name="Sender Email")
    cretaed_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    is_read = models.BooleanField(default=False, verbose_name="Read")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.title
