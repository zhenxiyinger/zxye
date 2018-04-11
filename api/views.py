import json
from django.http import HttpResponse


def index(request):
    resp = {'errorcode': 100, 'detail': '中文'}
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json")
