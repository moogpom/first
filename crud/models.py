from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50) #CharField: 제한있는 문자열
    pub_date=models.DateTimeField()
    writer=models.ForeignKey('user.SonUser', on_delete=models.CASCADE, null=False)
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=False,null=False)
    #아래 함수는 밑에서 설명
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]


class Bookmark(models.Model):
    
    postId = models.ForeignKey("Photo",on_delete=models.CASCADE,db_column="postId")
    userId=models.ForeignKey('user.SonUser', on_delete=models.CASCADE, null=False)
    #아래 함수는 밑에서 설명
    def __str__(self):
        return self.postId

