from django.db import models

# Create your models here.
class Request(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)