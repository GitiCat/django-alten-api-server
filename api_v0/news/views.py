from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import News
from .serializers import NewsSerializer

@csrf_exempt
def news_list(request):
    if request.methon == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.methon == 'POST':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)