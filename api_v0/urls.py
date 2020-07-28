from django.urls import path, re_path

from .article.views import article_list, category_article_list
from .images.views import gallery_list, images_list
from .news.views import news_list

urlpatterns = [
    path('articles/', article_list),
    path('categories-article', category_article_list),
    path('images/', images_list),
    path('gallery/', gallery_list),
    path('news/', news_list)
]