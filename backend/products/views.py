from rest_framework import  generics, mixins #authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

# from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin
from .models import Product
# from ..api.permissions import IsStaffEditorPermission
from . serializers import ProductSerializer

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes =[
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    #     ]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        #send a django signal

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()



# class ProductListAPIView(generics.ListAPIView):
#     """
#     not going to use it here
#     because we can add it to the create view
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# product_list_view = ProductListAPIView.as_view()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "awesome view"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method #PUT -> update #DESTROY -> delete 

    if method == "GET":
        if pk is not None:
            # detail view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404
            # return Response()
        #get request -> detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        #create item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)