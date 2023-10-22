from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Product  # Make sure to import your Product model
from .serializer import ProductSerializer  # Import the serializer you created earlier

@csrf_exempt  # Use this decorator to disable CSRF protection (for development)
def create_product(request):
    if request.method == 'POST':
        data = request.POST
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)
def retrieve_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)
@csrf_exempt
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = request.POST
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)
