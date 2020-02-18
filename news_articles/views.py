from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import NewsArticle


def news_list(request):
    news_articles = NewsArticle.objects.all()
    context = {
        'news_articles' : news_articles
    }
    return render(request,'news/list.html', context)


def news_article(request, news_article_id):
    news_article = get_object_or_404(NewsArticle, pk=news_article_id)
    context = {
        'news_article': news_article
    }
    return render(request, 'news/news_article.html', context)
