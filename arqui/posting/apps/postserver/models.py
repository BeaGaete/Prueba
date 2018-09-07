from django.db import models

# Create your models here.

class Post(models.Model):
    texto = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def text_output(self):
        return self.texto

    def __str__(self):
        return self.text_output()
