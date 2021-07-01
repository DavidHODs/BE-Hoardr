from django.shortcuts import render
from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.response import Response
from .models import Item, Image, Free_exercise
from .serializers import ItemSerializer, ImageSerializer, FreeExerciseSerializer, ItemIDSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.order_by('-uploaded_date')
    serializer_class = ItemSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]#, filters.OrderingFilter
    filterset_fields = ['category', 'price', 'is_favourite']
    search_fields = ['title', 'location']
    # ordering_fields = ['uploaded_date']
    lookup_fields = 'id'

class ItemIDViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemIDSerializer

    # def get_queryset(self):
    #     # id = self.request.query_params.get('id', None)
    #     # if id:
    #     single_item = Item.objects.get(id=kwargs['pk'])
    #     return single_item

    def list(self, request, *args, **kwargs):
        # item =  Item.objects.get(id=-1)
        # import pdb; pdb.set_trace()
        # serializer = ItemIDSerializer(item, many=True)
        return Response([])

    def retrieve(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = ItemIDSerializer(item)
        return Response(serializer.data)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class FreeExerciseViewSet(viewsets.ModelViewSet):
    queryset = Free_exercise.objects.all()
    serializer_class = FreeExerciseSerializer
