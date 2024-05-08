from django.db import models
from django.contrib.auth.models import User

##################  BLOG MODEL #########################

class Blog(models.Model):
    title=models.CharField(max_length=100)
    img=models.FileField(upload_to='blog_img')
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
