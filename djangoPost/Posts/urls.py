from django.contrib import admin
from django.urls import path,include
#from other_app.views import Home
from . import views


urlpatterns = [
    #path('', Home.as_view(), name='home')
    path('', views.home, name='home'),
    path('posts/create', views.create_post, name='post-create'),
    path('about/', views.about, name = 'about')
]