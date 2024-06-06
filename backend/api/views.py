# import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    #if request.method != "POST":
    #    return Response({"detail": "GET not allowed"}, status=405)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
       # data = model_to_dict(instance, fields=['id', 'title', 'price', 'discount_price', "get_discount_val"])
      #  data = model_to_dict(model_data)
      # ***************** instance
    #    data['id'] = model_data.id
    #    data['title'] = model_data.title
    #    data['content'] = model_data.content
    #    data['price'] = model_data.price
        """
        serialization:
        # model instance (model_data)
        # turn a Python dict
        # return Json to my client
        """
    #return JsonResponse(data)
    return Response(data)
"""
def api_home(request, *args, **kwargs):
    # print(dir(request))
    print(request.GET) # url query params
    print(request.POST)
    body = request.body # byte string of json data
    data = {}
    try:
        data = json.loads(body) # string of json data -> python dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    # print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
"""