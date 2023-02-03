from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class SonUser(AbstractUser):
    introduce =  models.TextField()
    dog = models.BooleanField(blank=True,null=True)
    LIKE_CHOICES = (
		('도자기', '도자기'),
    ('수채화', '수채화'),
    ('유화', '유화'),
    ('자수', '자수'),
    ('뜨개질', '뜨개질'),
    ('레진아트', '레진아트'),('강아지', '강아지와 함께하는 공예시간'),
  )
    like = models.CharField(max_length=5, choices=LIKE_CHOICES)