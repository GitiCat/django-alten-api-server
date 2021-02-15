from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Personnel, Department
from .serializers import PersonnelSerialize, DeparmentSerialize

def personnel_list(request):
    if request.method == 'GET':
        personnel = Personnel.objects.all()
        serializer = PersonnelSerialize(personnel, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonnelSerialize(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

def department_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DeparmentSerialize(department, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeparmentSerialize(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)