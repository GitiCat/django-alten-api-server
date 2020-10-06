from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from .models import Publication
from .serializers import PublicationSerializer

@csrf_exempt
def publication_liss(request):
    if request.method == 'GET':
        if request.GET:
            query_id = request.GET.get('id')
            publication = Publication.objects.filter(id=query_id)

            if not publication:
                return JsonResponse({
                    'string': 'Publication with id {0} is not found...'.format(query_id),
                    'status_code': 404
                }, status=404, safe=False)

            serializer = PublicationSerializer(publication, many=True)
            return JsonResponse(serializer.data, safe=False)

        publication = Publication.objects.all()
        serializer = PublicationSerializer(publication, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)