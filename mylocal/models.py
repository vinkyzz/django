from django.db import models

class Post(models.Model):
    title = models.CharField('Name',max_length=50)
    post=models.TextField('discription')
    def __str__(self):
        return self.title