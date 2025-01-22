"""
URL configuration for projectForum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ForumApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='Start page'),
    ####################
    path('signup/', views.register_user, name='signup'),
    path('category/<int:category_id>/posts/', views.category_posts, name='category_posts'),
    path('account/', include("django.contrib.auth.urls")),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_category, name='add_category'),
    ####################
    path('user/<int:user_id>', views.user_profile_details, name='user_profile_details'),
    path('edit-user/<int:user_id>', views.user_profile_edit, name='user_profile_edit'),
    path('posts/<int:post_id>/full/', views.full_post,name='full_post'),
    ####################
    path('category/<int:category_id>/add-post/', views.add_post, name='add_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    ####################
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
