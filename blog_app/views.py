from django.shortcuts import render
from .models import Category, Blog


# Create your views here.
def blog(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True)
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
    }
    return render(request, 'blog.html', context)
