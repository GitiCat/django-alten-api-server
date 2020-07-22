from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Gallery, Images
from .serializers import GallerySerialize, ImagesSerializer

@csrf_exempt
def gallery_list(request):
    if request.method == 'GET':
        gallery = Gallery.objects.all()
        serializer = GallerySerialize(gallery, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GallerySerialize(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

@csrf_exempt
def images_list(request):
    if request.method == 'GET':
        images = Images.objects.all()
        serializer = ImagesSerializer(images, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImagesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)