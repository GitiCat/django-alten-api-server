from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article, CategoryArticle
from .serializers import ArticleSerializer, CategoryArticleSerializer

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.methon == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors)

@csrf_exempt
def category_article_list(request):
    if request.method == 'GET':
        category = CategoryArticle.objects.all()
        serializer = CategoryArticleSerializer(category, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.methon == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoryArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)