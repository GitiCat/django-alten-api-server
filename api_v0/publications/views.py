from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from .models import Publication
from ..files.models import File
from .serializers import PublicationSerializer
from ..files.serializers import FileSerializer

@csrf_exempt
def publication_liss(request):
    if request.method == 'GET':
        if request.GET:
            query = request.GET
            publications = Publication.objects.filter(id=query['id'])

            if not publications:
                return JsonResponse({
                    'error_string': 'Publication with id {0} is not found...'.format(query['id']),
                    'status_code': 404
                }, status=404, safe=False)

            data = get_json_publications(publications)
            return JsonResponse(data, safe=False)

        publications = Publication.objects.all()
        data = get_json_publications(publications)

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

def get_json_publications(obj):
    data = PublicationSerializer(obj, many=True).data
    arr = []
    arr_item = {}

    for item in data:
        arr_item = {
            'category': item['category'],
            'name': item['name'],
            'title': item['title'],
            'subtitle': item['subtitle'],
            'descriptor': item['descriptor'],
            'image': item['main_image'],
            'files': [],
            'origin_url': item['url'],
            'is_active': item['is_active'],
            'created_at': item['created_at']
        }
        list_file = File.objects.filter(list_files=item['files'])
        list_file_data = FileSerializer(list_file, many=True)
        arr_files = []

        for file in list_file_data.data:
            arr_files.append(file)

        arr_item['files'] = arr_files
        arr.append(arr_item)

    return arr