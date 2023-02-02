from django.db import models
from imagekit import processors
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class Book(models.Model):
    
    title = models.CharField(max_length=50)
    writer=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    new_date = models.DateTimeField()
    pub_date=models.CharField(max_length=30)
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=True,null=True)
    image_thumbnail = ImageSpecField(source = 'image',processors=[ResizeToFill(120,200)])
   
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] 
