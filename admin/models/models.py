from django.db import models


class UserUsers(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    salt = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    created = models.IntegerField

    class Meta:
        db_table = 'xy_user_users'


class CmsSetting(models.Model):
    user_id = models.IntegerField()
    link_id = models.IntegerField()

    class Meta:
        db_table = 'wm_user_banks_del'
        app_label = 'yinduo'
