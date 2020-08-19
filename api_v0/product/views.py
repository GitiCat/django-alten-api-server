from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Product, CategoryProduct
from .serializers import ProductSerializer, CategoryProductSerializer

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

@csrf_exempt
def category_product_list(request):
    if request.method == 'GET':
        categories = CategoryProduct.objects.all()
        serializer = CategoryProductSerializer(categories, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoryProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

def products_by_category_list(request):
    if request.method == 'GET':
        categories = CategoryProduct.objects.all().order_by('created_at')
        products = Product.objects.all()

        categories_serializer = CategoryProductSerializer(categories, many=True)
        products_serializer = ProductSerializer(products, many=True)

        data = []
        category_arr = {}

        for category in categories_serializer.data:
            category_arr = {
                'title': category['title'],
                'descriptor': category['descriptor'],
                'items': []
            }

            products_by_category = products.filter(category=category['id'])

            for product in products_by_category:
                category_arr['items'].append(product)
            
            data.append(category_arr)
        
        return JsonResponse(data=data, safe=False)