from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from items.models import Item
from .serializers import ItemSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
