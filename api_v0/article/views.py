from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from .models import Article, CategoryArticle
from .serializers import ArticleSerializer, CategoryArticleSerializer

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        if request.GET:
            query = request.GET
            
            try:
                category_obj = CategoryArticle.objects.get(name=query['category']);
            except ObjectDoesNotExist:
                return JsonResponse({
                    'string': 'Category {0} is not found...'.format(query['category']),
                    'status_code': 404
                }, status=404, safe=False);

            specifical_articles = Article.objects.filter(category=category_obj.id)

            if not specifical_articles:
                return JsonResponse({
                    'message': 'Articles with category {0} not found...'.format(query['category']),
                    'status_code': 404
                }, status=404, safe=False)

            if request.GET.get('id'):
                id_article = specifical_articles.filter(id=query['id'])

                if not id_article:
                    return JsonResponse({
                        'string': 'Article with category {0} by id {1} not found...'.format(query['category'], query['id']),
                        'status_code': 404
                    }, status=404, safe=False)

                serializer = ArticleSerializer(id_article, many=True)
                return JsonResponse({
                    'category': {
                        'name': category_obj.name, 
                        'title': category_obj.title,
                        'descriptor': category_obj.descriptor
                    },
                    'data': serializer.data
                })

            serializer = ArticleSerializer(specifical_articles.order_by('id'), many=True)
            return JsonResponse({
                'category': {
                    'name': category_obj.name, 
                    'title': category_obj.title,
                    'descriptor': category_obj.descriptor
                },
                'data': serializer.data
            }, safe=False)
        
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