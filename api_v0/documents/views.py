from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Document, CategoryDocuments
from .serializers import DocumentSerializer, CategoryDocumentsSerializer

@csrf_exempt
def documents_list(request):
    if request.method == 'GET':
        documents = Document.objects.all()

        data = []
        category_arr = {}

        categories = CategoryDocuments.objects.all()
        category_data = CategoryDocumentsSerializer(categories, many=True).data
        
        for category in category_data:
            category_arr = {
                'title': category['title'],
                'descriptor': category['descriptor'],
                'items': []
            }

            documents_on_category = documents.filter(category=category['id']).order_by('created_at')
            document_data = DocumentSerializer(documents_on_category, many=True).data
            document_arr = []
            
            for document in document_data:
                document_arr.append(document)

            category_arr['items'] = document_arr
            data.append(category_arr)

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DocumentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

@csrf_exempt
def category_document_list(request):
    if request.method == 'GET':
        category = CategoryDocuments.objects.all()
        serializer = CategoryDocumentsSerializer(category, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoryDocumentsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)