from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Personnel, Department
from .serializers import PersonnelSerialize, DepartmentSerialize

def personnel_list(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        department_data = DepartmentSerialize(departments, many=True).data

        data = []
        department_arr = {}

        for department in department_data:
            deparment_arr = {
                'name': department['name'],
                'descriptor': department['descriptor'],
                'items': []
            }

            personnels = Personnel.objects.filter(department=department['id']).order_by('created_at')
            personnels_data = PersonnelSerialize(personnels, many=True).data
            personnels_arr = []

            for person in personnels_data:
                personnels_arr.append(person)

            deparment_arr['items'] = personnels_arr
            data.append(deparment_arr)

        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonnelSerialize(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)