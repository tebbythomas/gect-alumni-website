from django.urls import path

from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:news_article_id>', views.news_article, name='news_article'),
]