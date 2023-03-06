from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/new/', views.post_new, name='post_new'),
]