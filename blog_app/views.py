from django.shortcuts import render
from .models import Category


# Create your views here.
def blog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog.html', context)
