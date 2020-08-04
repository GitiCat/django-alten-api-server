from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import News
from .serializers import NewsSerializer

@csrf_exempt
def news_list(request):
    if request.method == 'GET':
        if request.GET.get('id'):
            item_id = request.GET.get('id')
            item = News.objects.filter(id=item_id)

            if not item:
                return JsonResponse({
                    'error': 'News by id: {0} not found...'.format(item_id),
                    'status_code': 404
                }, status=404, safe=False)

            serializer = NewsSerializer(item, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)