from django.shortcuts import redirect, render
from .models import Post, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(response):
    posts = Post.objects.all().order_by("-date")
    content = {"posts" : posts}
    return render(response, 'home.html', content)

def articleView(response, pk):
    post = Post.objects.get(pk=pk)
    content = {"post":post}
    return render(response, 'article.html', content)

def categoryView(response, title):
    categoryPost = Post.objects.filter(category__title__contains=title)
    content = {"categoryPost": categoryPost.order_by("-date"), "title": title}
    return render(response, 'categoryView.html', content)

def categoryList(response):
    categories = Category.objects.all().order_by("title")
    catList = {"categories" : categories}
    return render(response, 'categoryList.html', catList)

def loginPage(response):
    return render(response, 'loginPage.html')

def signUpPage(response):
    return render(response, 'signUpPage.html')

def loggedIn(response):
    if response.method=='POST':
        username = User.objects.get(username=response.POST['uname'])
        password = response.POST['pword']
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            messages.success(response, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(response, "Username and password doesn't match!")
            return redirect('loginPage')
    else:
        return redirect('loginPage')

def logOut(response):
    logout(response)
    messages.success(response, "Logged out successfully!")
    return redirect('home')

def signedUp(response):
    if response.method=='POST':
        username = response.POST['username']
        firstName = response.POST['fname']
        lastName = response.POST['lname']
        email = response.POST['email']
        password = response.POST['password']
        cpassword = response.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(response, "Username alreay exists!")
                return redirect('signUpPage')
            elif User.objects.filter(email=email).exists():
                messages.error(response, "Email already taken!")
                return redirect('signUpPage')
            else:
                user = User.objects.create_user(username, email, password)
                user.first_name = firstName
                user.last_name = lastName
                user.save()
                messages.success(response, "Signed up successfully!")
                return redirect('loginPage')
        else:
            messages.error(response, "Password doesn't match")
            return redirect('signUpPage')
    else:
        return render(response, 'errorPage.html')


def addPostPage(response):
    category = Category.objects.all().order_by("title")
    content = {"categories" : category}
    return render(response, 'addPost.html', content)


def addPost(response):
    if response.method == 'POST':
        title = response.POST["title"]
        category = Category.objects.get(title = response.POST["category"])
        content = response.POST["content"]
        author = response.user
        post = Post.objects.create(title=title, category=category, content=content, author=author)
        post.save()
        return redirect('home')
    else:
        return redirect('loginPage')

def userProfile(response, username):
    userPosts = Post.objects.filter(author__username__contains=username).order_by("-date")
    profileuser = User.objects.get(username=username)
    content = {"blogs" : userPosts, "profileuser":profileuser }
    return render(response, 'userPage.html', content)

def deletePage(response, pk):
    post = Post.objects.get(pk=pk)
    content = {"post" : post}
    return render(response, 'deleteView.html', content)

def deletePost(response, pk):
    if response.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        if post.author == response.user:
            post.delete()
            messages.success(response, "Post deleted successfully!")
            return redirect("home")
        else:
            return render(response, 'errorPage.html')
    else:
        return render(response, 'errorPage.html')

def updatePage(response, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all().order_by("title")
    content = {"post":post, "categories": categories}
    return render(response, 'updateBlog.html', content)

def updatePost(response, pk):
    if response.method == "POST":
        post = Post.objects.get(pk=pk)
        post.title = response.POST['updateTitle']
        post.category = Category.objects.get(title = response.POST['updateCategory'])
        post.content = response.POST['updateContent']
        post.save()
        return redirect("articleView", pk)