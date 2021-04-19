from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Personnel, Department, CommunicationMethod
from .serializers import PersonnelSerialize, DepartmentSerialize, CommunicationMethodSerializer

def personnel_list(request):
    if request.method == 'GET':
        communication_methods = CommunicationMethod.objects.all().order_by('created_at')
        communication_methods_serializer = CommunicationMethodSerializer(communication_methods, many=True)

        data = []
        item_arr = {}

        for communication_method in communication_methods_serializer.data:
            item_arr = {
                'is_visible': communication_method['is_visible'],
                'name': communication_method['name'],
                'descriptor': communication_method['descriptor'],
                'responsible': communication_method['responsible'],
                'position': communication_method['position'],
                'phone': communication_method['phone'],
                'is_phone_visible': communication_method['is_phone_visible'],
                'fax': communication_method['fax'],
                'is_fax_visible': communication_method['is_fax_visible'],
                'email': communication_method['email'],
                'is_email_visible': communication_method['is_email_visible'],
                'personnels': [],
                'created_at': communication_method['created_at']
            }

            personnels = Personnel.objects.filter(communication_method=communication_method['id']).order_by('created_at')
            personnels_serializer = PersonnelSerialize(personnels, many=True)

            for person in personnels_serializer.data:
                item_arr['personnels'].append(person)

            data.append(item_arr)

        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonnelSerialize(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)