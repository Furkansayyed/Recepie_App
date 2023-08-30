from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RecpieUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)
    recepie_image = models.ImageField(upload_to='recepies')

    def __str__(self) -> str:
        return self.title
    
