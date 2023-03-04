from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def homepage(request):
    posts = Post.objects.all().order_by('published_date')
    context = {'posts': posts}
    return render(request, 'homepage.html', context)