from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from .models import Product, CategoryProduct
from .serializers import ProductSerializer, CategoryProductSerializer

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        if request.GET:
            query = request.GET

            products = Product.objects.filter(category=query['category'])

            if not products: 
                return JsonResponse({
                    'string': 'Products with category {0} is not found...'.format(query['category']),
                    'status_code': 404
                }, status=404, safe=False)
            
            serializer = ProductSerializer(products, many=True)

            return JsonResponse(serializer.data, safe=False)
        
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
        products = Product.objects.all().order_by('created_at')

        categories = CategoryProduct.objects.all()
        categories_serializer = CategoryProductSerializer(categories, many=True)
        categories_data = categories_serializer.data

        returned_data = []
        category_item = {}
        
        for category in categories_data:
            category_item = {
                'id': category['id'],
                'title': category['title'],
                'descriptor': category['descriptor'],
                'items': []
            }

            products_in_category = products.filter(category=category['id'])
            products_serializer = ProductSerializer(products_in_category, many=True)
            products_data = products_serializer.data

            for product in products_data:
                category_item['items'].append({
                    'id': product['id'],
                    'title': product['title'],
                    'descriptor': product['descriptor'],
                    'feature': product['feature'],
                    'image': product['main_image'],
                    'file': product['file']
                })
            returned_data.append(category_item)

        return JsonResponse(returned_data, safe=False)