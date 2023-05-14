from .models import Article
from django.shortcuts import render


def archive(request):
    return render(request, 'archive.html', {
                                                "posts": Article.objects.all().order_by('-created_date'),
                                                "user": request.user
                                            })
