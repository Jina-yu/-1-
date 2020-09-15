from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta():
        db_table = '게시글'
        verbose_name ='게시글'
        verbose_name_plural = '게시글'

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

