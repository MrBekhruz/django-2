from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Post)


class PostModel(admin.ModelAdmin):
    post_date = models.DateField(auto_now = False)
    list_display = ('post_title ',' post_image','post_content','post_hashtag',' post_date',)
    list_filter = ('post_hashtag')


admin.site.register(PostCategory)
