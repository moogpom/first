from django.db import models
from imagekit.models import ImageSpecField # 이 함수로 썸네일 만듦
from imagekit.processors import ResizeToFill #크기 조절
# Create your models here.
class PomBlog(models.Model):
    title = models.CharField(max_length=200) #CharField: 제한있는 문자열
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=False,null=False)
    image_thumbnail = ImageSpecField(source = 'image',processors=[ResizeToFill(200,200)])
#,blank=True,null=True 는 비어있을 수 있다고 설정해주는 거임


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] 