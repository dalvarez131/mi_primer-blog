from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Post

def post_list(request):
    tiempo_necesario=timezone.now()-timedelta(days=1)
    posts=Post.objects.filter (published_date__range=[tiempo_necesario, timezone.now()]).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
# Create your views here.
