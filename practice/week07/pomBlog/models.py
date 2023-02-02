from django.db import models

# Create your models here.
class PomBlog(models.Model):
    title = models.CharField(max_length=200) #CharField: 제한있는 문자열
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:40] 
