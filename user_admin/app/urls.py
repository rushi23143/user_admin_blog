from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.modules, name='modules'),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/', views.logout, name='logout'),
    path('index/',views.index, name="index"),
    path('blog/',views.blog, name="blog"),
    path('edit_blog/<int:id>/', views.edit_blog, name='editblog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='deleteblog'),
    path('del_blog/<int:id>/', views.del_blog, name='delblog'),
    #####Admin########
    path('admin_page/',views.admin_page, name="admin_page"),
    path('users/',views.users, name="users"),
    path('user_blog/', views.user_blog, name='user_blog'),
]