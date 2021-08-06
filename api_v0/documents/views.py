from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Document, CategoryDocuments
from .serializers import DocumentSerializer, CategoryDocumentsSerializer

@csrf_exempt
def documents_list(request):
    if request.method == 'GET':
        if request.GET:
            # Selected data array from database
            categories = CategoryDocuments.objects.all()
            data = []
            query_category = None 
            query_excludes = None
            
            query = request.GET
            if 'category' in query: query_category = query['category']
            if 'excludes' in query: query_excludes = query.getlist('excludes')

            if query_category:
                categories = categories.filter(name=query_category)

            if query_excludes:
                for exclude in query_excludes:
                    categories = categories.exclude(name=exclude)

            if not categories:
                return JsonResponse({
                    'string': 'Categories documents with name {0} is not found...'.format(query_category),
                    'status_code': 404
                }, status=404, safe=False)

            serializer = CategoryDocumentsSerializer(categories, many=True)
            data = get_data_json(serializer.data)
            return JsonResponse(data, safe=False)
            
        categories = CategoryDocuments.objects.all()
        serializer = CategoryDocumentsSerializer(categories, many=True)
        data = get_data_json(serializer.data)
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
            'id': child_category['id'],
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
    category_arr = {}
    if not category['root_category']:
        category_arr = {
            'id': category['id'],
            'name': category['name'],
            'title': category['title'],
            'descriptor': category['descriptor'],
            'documents': get_documents_by_category_id(category['id']),
            'childs': []
        }

        category_arr['childs'] = formation_childs_element(category)

    return category_arr

def get_data_json(data): 
    result = []
    
    for item in data:
        arr = formation_document_list(item)
        if arr:
            result.append(arr)

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