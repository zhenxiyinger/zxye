from rest_framework.decorators import api_view
from django.http import HttpResponse
import json


@api_view(['GET', 'POST'])
def index(request):
    resp = {'errorcode': 100, 'detail': '中文'}
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json")
