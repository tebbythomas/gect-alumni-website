from django.shortcuts import render
from django.http import HttpResponse
from gallery_pics.models import GalleryPic
from news_articles.models import NewsArticle
from members.models import Member


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
    electrical_members = Member.objects.filter(branch="electrical")
    mechanical_members = Member.objects.filter(branch="mechanical")
    civil_members = Member.objects.filter(branch="civil")
    chemical_members = Member.objects.filter(branch="chemical")
    production_members = Member.objects.filter(branch="production")
    print(f"Num of electrical members: {len(electrical_members)}")
    print(f"Num of mechanical members: {len(mechanical_members)}")
    print(f"Num of civil members: {len(civil_members)}")
    print(f"Num of chemical members: {len(chemical_members)}")
    print(f"Num of production members: {len(production_members)}")
    total_registered = len(electrical_members) + len(mechanical_members) + len(production_members) + len(civil_members) + len(chemical_members)
    context = {
        "count_electrical" : len(electrical_members),
        "count_mechanical" : len(mechanical_members),
        "count_civil" : len(civil_members),
        "count_chemical" : len(chemical_members),
        "count_production" : len(production_members),
        "total_registered" : total_registered,
        "total_chemical_strength" : 45,
        "total_civil_strength" : 58,
        "total_production_strength" : 14,
        "total_electrical_strength" : 42,
        "total_mechanical_strength" : 49,

    }
    return render(request, 'pages/stats.html', context)