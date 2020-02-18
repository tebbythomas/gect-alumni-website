from django.shortcuts import render
from django.http import HttpResponse
from gallery_pics.models import GalleryPic
from news_articles.models import NewsArticle


def index(request):
    news_articles = NewsArticle.objects.all()[:2]
    banner_pics = GalleryPic.objects.all().filter(is_banner=True)
    context = {
        'news_articles' : news_articles,
        'banner_pics' : banner_pics,
    }
    return render(request, 'pages/index.html', context)


def stats(request):
    # news_articles = NewsArticle.objects.all()[:2]
    # banner_pics = GalleryPic.objects.all().filter(is_banner=True)
    # context = {
    #     'news_articles' : news_articles,
    #     'banner_pics' : banner_pics,
    # }
    context = {
        
    }
    return render(request, 'pages/stats.html', context)