import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
      #  data = model_to_dict(model_data)
      # *****************
    #    data['id'] = model_data.id
    #    data['title'] = model_data.title
    #    data['content'] = model_data.content
    #    data['price'] = model_data.price
    # a small change to test the repo pull
        """
        serialization:
        # model instance (model_data)
        # turn a Python dict
        # return Json to my client
        """
    return JsonResponse(data)
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