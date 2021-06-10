from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Vacancies
from .serializers import VacanciesSerializer

@csrf_exempt
def news_list(request):
    if request.method == "GET":
        if request.GET:
            query = request.GET
            vacancy = Vacancies.objects.filter(id = query['id'])

            if not vacancy:
                return JsonResponse({
                    'string': 'Vacancy with id {0} is not found'.format(query['id']),
                    'status_code': 404
                }, status=404, safe=False)

            serialize = VacanciesSerializer(vacancy, many=True)
            return JsonResponse(serialize.data, safe=False)

        model = Vacancies.objects.all()
        serialize = VacanciesSerializer(model, many=True)
        return JsonResponse(serialize.data, safe=False)

    elif request.method == 'POST':
        body = JSONParser().parse(request)
        serialize = VacanciesSerializer(data=body)

        if(serialize.is_valid()):
            serialize.save()
            return JsonResponse(serialize.data)

        return JsonResponse(serialize._errors)