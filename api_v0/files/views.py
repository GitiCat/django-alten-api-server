from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import File, ListFiles
from .serializers import FileSerializer, ListFilesSerializer

@csrf_exempt
def files_list(request):
    if request.method == 'GET':
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

@csrf_exempt
def list_files_list(request):
    if request.method == 'GET':
        lists_files = ListFiles.objects.all()
        serializer = ListFilesSerializer(lists_files, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListFilesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)