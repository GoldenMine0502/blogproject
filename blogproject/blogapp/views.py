from django.shortcuts import render, redirect
from django.utils import timezone
from blogapp.models import Blog
from .forms import BlogForm, BlogModelForm


# Create your views here.
def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})


# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')


# 블로그 글을 저장해주는 함수
def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')


# django form을 이용해 입력값 받기
# get요청 (입력값을 받을 수 있는 html을 갖다 줘야함)
# post요청 (입력한 내용을 데이터베이스에 저장)
# 같은 url에서 둘다 처리 가능
def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장

        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다 주기
        form = BlogForm()

    return render(request, 'form_create.html', {'form': form})


def modelformcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다 주기
        form = BlogForm()

    return render(request, 'form_create.html', {'form': form})