from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def homepage(request):
    posts = Post.objects.all().order_by('published_date')
    #the step below makes all the post objects created above 
    # a value to the key "posts" in context, so that they can be accessed in the view.
    context = {'posts': posts}
    return render(request, 'homepage.html', context)

def FormView():
    pass
