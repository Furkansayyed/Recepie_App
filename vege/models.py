from django.db import models

# Create your models here.
class RecpieUpload(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)
    recepie_image = models.ImageField(upload_to='recepies')

    def __str__(self) -> str:
        return self.title
    
