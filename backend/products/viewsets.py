from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer


# can be used in views.py
class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> Product instance detail view
    post -> create -> new instance
    put -> update
    patch -> partial update
    destroy -> delete
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    ):
    """
    get -> list -> queryset
    get -> retrieve -> Product instance detail view
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})