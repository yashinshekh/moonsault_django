from django.db import models

class Item(models.Model):
    text = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='items/',null=True,blank=True)

    def __str__(self):
        return self.text
