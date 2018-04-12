from django.urls import path
from api.views import index, activity

urlpatterns = [
    path('index/index/', index.index),
    path('activity/index/', activity.index),
]
