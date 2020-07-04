from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    email=models.EmailField()
    query=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class doubts_data(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    doubt_language=models.CharField(max_length=30)
    doubt_text=models.TextField()
    doubt_code=models.TextField()
    author=models.CharField(max_length=30)
    slug=models.SlugField()
    doubt_file=models.FileField(upload_to='static/doubt_files',blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class comments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(doubts_data,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'By '+self.user.username



