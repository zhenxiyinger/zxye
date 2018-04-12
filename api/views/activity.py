from rest_framework.decorators import api_view
from django.http import HttpResponse
import json


@api_view(['GET', 'POST'])
def index(request):
    resp = {'errorcode': 100, 'detail': '活动'}
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json")
