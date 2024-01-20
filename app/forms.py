from django import forms
from .models  import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'



class PostForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'