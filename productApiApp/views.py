
from asyncio.windows_events import NULL
from email.policy import strict
from urllib import response
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json 

from  .models import Product

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ProductView(View):
    #post data api
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        product_name = data[0]['product_name']
        product_price = data[0]['product_price']
        product_quantity = data[0]['product_quantity']

        product_data = {
            'product_name' : product_name,
            'product_price' : product_price,
            'product_quantity': product_quantity,
        }

        product = Product.objects.create(**product_data)
        data = json.loads(serializers.serialize('json', [product]))
      
       
        return JsonResponse(data, safe=False)

    #Get all data api
    def get(self, request):
        product_count = Product.objects.count()
        products = Product.objects.all()

        products_data = []

        for product in products:
            products_data.append({
                'product_id' : product.pk,
                'product_name':product.product_name,
                'product_price':product.product_price,
                'product_quantity':product.product_quantity
            })
        
        data = {
            "products":products_data,
            "products_count":product_count
        }

        return JsonResponse (data)


@method_decorator(csrf_exempt, name='dispatch')
class ProductUpdate(View):
    #Update Product request
    def put(self, request, product_pk):
        data = json.loads(request.body.decode('utf-8'))
        product = Product.objects.get(id = product_pk)
        product.product_name = data[0]['product_name']
        product.product_price = data[0]['product_price']
        product.product_quantity = data[0]['product_quantity']
        
        

        product.save()

        return JsonResponse({"message":"successfully Updated"})

    #Delete a product request
    def delete(self, request, product_pk ):
          
            product = Product.objects.get(id=product_pk)
            product.delete()
               
            return JsonResponse({'message':f'{product.product_name} deleted Successfully'})
        
    
        

        
