from django.urls import path
from .views import index

urlpatterns = [
    path('index/index/', index.index, name='index_index'),
]
