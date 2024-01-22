from django.shortcuts import render
from .models import Article



def home_page(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'blog/home_page.html', context)


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'blog/article_page.html', context)