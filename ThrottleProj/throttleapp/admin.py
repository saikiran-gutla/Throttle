from django.contrib import admin
from .models import UserModel, ActivityPeriodModel


# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'real_name', 'tz', 'status']


class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ['User_id', 'start_time', 'end_time']


admin.site.register(UserModel, UsersAdmin)
admin.site.register(ActivityPeriodModel, ActivityPeriodAdmin)
