from django.db import models
from django.urls import reverse
from .forms import *


categorys = [
    ('sport xabarlari','sport xabarlari'),
    ('jaxon xabarlarr','jaxon xabarlari'),
    ('yurtimizda ro\y berayotgan sunngi xabarlari','yurtimizda ro\y berayotgan sunngi xabarlari'),
]


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    post_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    post_title = models.CharField(max_length = 255)
    post_image = models.TextField()
    post_content = models.TextField()
    post_hashtag = models.CharField(max_length = 255)
    post_date = models.DateField(auto_now = True)

    def __str__(self):
        return self.post_hashtag
    

class PostCategory(models.Model):
    post_category  = models.ForeignKey(Category,on_delete = models.CASCADE)
    post_title = models.CharField(max_length = 255)
    post_image = models.TextField()
    post_content = models.TextField()
    post_hashtag = models.CharField(max_length = 255)
    post_date = models.DateField(auto_now = True)

    def __str__(self):
        return self.post_title
    

    def get_obsolyut_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
    

class Students(models.Model):
    st_password = models.CharField(max_length = 255)