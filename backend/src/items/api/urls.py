from django.urls import path

from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view()),
    path('<pk>', ItemDetailView.as_view())
]