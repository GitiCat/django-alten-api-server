from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Document, CategoryDocuments
from .serializers import DocumentSerializer, CategoryDocumentsSerializer

@csrf_exempt
def documents_list(request):
    if request.method == 'GET':
        categories = CategoryDocuments.objects.all()

        data = []
        categories_serialize = CategoryDocumentsSerializer(categories, many=True)

        for category in categories_serialize.data:
            arr = formation_document_list(category)
            if arr:
                data.append(formation_document_list(category))

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DocumentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

def get_documents_by_category_id(id):
    result = []

    documents = Document.objects.filter(category=id)
    data = DocumentSerializer(documents, many=True).data

    if data:
        for item in data:
            result.append(item)

    return result

def formation_childs_element(category):
    result = []
    
    child_categories = CategoryDocuments.objects.filter(root_category=category['id'])

    if not child_categories:
        return None
    
    child_categories_data = CategoryDocumentsSerializer(child_categories, many=True).data
    
    for child_category in child_categories_data:
        arr = {
            'title': child_category['title'],
            'descriptor': child_category['descriptor'],
            'documents': get_documents_by_category_id(child_category['id']),
            'childs': []
        }

        if CategoryDocuments.objects.filter(root_category=child_category['id']):
            arr['childs'] = formation_childs_element(child_category)
        else:
            arr['childs'] = None
        
        result.append(arr)

    return result

def formation_document_list(category):
    result = []
    if not category['root_category']:
        category_arr = {
            'title': category['title'],
            'descriptor': category['descriptor'],
            'documents': get_documents_by_category_id(category['id']),
            'childs': []
        }

        category_arr['childs'] = formation_childs_element(category)
        result.append(category_arr)

    return result

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