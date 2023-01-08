from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('post/<str:pk>', views.post, name='post')
]
