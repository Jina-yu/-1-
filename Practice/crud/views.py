from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Article, Blog
from django.utils import timezone
from .forms import NewBlog

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['re_password']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('index')
    return render(request,'signup.html')



def index(request):
    contents = reversed(Article.objects.all())
    return render(request, 'index.html',{'contents': contents})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'login.html', {'error' : '아이디나 비밀번호가 틀렸습니다.'})
    else :
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def create(request):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('create')
    else:
        #단순히 입력받을 수 있는 form을 띄어줘라
        form = NewBlog()
        return render(request, 'create.html', {'form':form})

def create_article(request):
    article = Article()
    article.title = request.GET['title']
    article.content = request.GET['content']
    article.author = request.user
    article.save()
    return redirect('index')

def delete_article(request):
    article_id = request.GET['post_id']
    article = Article.objects.get(id = article_id)
    article.delete()
    return redirect('index')

def update(request):
    article_id = request.GET['post_id']
    article = Article.objects.get(id = article_id)
    form = NewBlog(request.POST, instance=blog)
    if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'article':article, 'form':form})

def update_article(request):
    article_id = request.GET['post_id']
    title = request.GET['title']
    content = request.GET['content']
    article = Article.objects.get(id = article_id)
    article.title = title
    article.content = content
    article.save()
    return redirect('index')
