from django.db import models

# Create your models here.
class Advocate(models.Model):
    username = models.CharField(max_length = 200)
    Bio = models.TextField(max_length = 500,null=True,blank = True)

    def __str__(self):
        return self.username