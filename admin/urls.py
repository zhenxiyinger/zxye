from django.urls import path
from admin.views import index

urlpatterns = [
    path('index/index/', index.index, name='index_index'),
    path('index/users/', index.users)
]
