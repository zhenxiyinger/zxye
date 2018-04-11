from django.shortcuts import render

from admin.models.models import UserUsers, CmsSetting


def index(request):
    return render(request, 'admin/index/index.html')


def users(request):
    user_list = CmsSetting.objects.all()
    print(user_list)
    return render(request, 'admin/index/users.html')
