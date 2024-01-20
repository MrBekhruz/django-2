from django.urls  import path
from .views import *

urlpatterns = [
    path('',home, name=home),
    path('news/<int:pk>/',get_post,name='post_detail'),
    path('create/' , postform , name = 'postcreate')
]
