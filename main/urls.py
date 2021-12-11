from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>', views.articleView, name="articleView"),
    path('categories', views.categoryList, name="categoryList"),
    path('categories/<str:title>', views.categoryView, name="categoryView"),
    path('login', views.loginPage, name="loginPage"),
    path('signUp', views.signUpPage, name="signUpPage"),
    path('loggedIn', views.loggedIn, name="loggedIn"),
    path('logOut', views.logOut, name="logOut"),
    path('signedUp', views.signedUp, name="signedUp"),
    path('add-post', views.addPostPage, name="addPost"),
    path('add-blog', views.addPost, name="addBlog"),
    path('user/<str:username>', views.userProfile, name="userProfile"),
    path('delete-blog/<int:pk>', views.deletePage, name="deletePage"),
    path('deletePost/<int:pk>', views.deletePost, name="deletePost"),
    path('update-post/<int:pk>', views.updatePage, name="updatePage"),
    path('updatePost/<int:pk>', views.updatePost, name="updatePost"),
]