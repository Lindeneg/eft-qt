from django.urls import path

from .views import ItemListView, ItemDetailView, ItemCreateView

urlpatterns = [
    path('', ItemListView.as_view()),
    path('create/', ItemCreateView.as_view()),
    path('<pk>', ItemDetailView.as_view())
]