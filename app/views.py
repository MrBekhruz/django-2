from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse

def home(request):
    post = Post.objects.all()


    context = {
        'post': post
    }
    return render(request, 'index.html',context)

def get_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        'post':post
    }
    return render(request,'page2.html',context)

def postform(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        

        else:
            form = PostForm()
            return render(request,'page3.html',{'form':form})