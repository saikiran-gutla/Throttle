from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import UsersList, Usersapi, ActivityPeriodapi

router = DefaultRouter()
router.register("User", Usersapi)
router.register("ActivityPeriod", ActivityPeriodapi)

urlpatterns = [
    url(r'^all_users/', UsersList.as_view()),
    url('nested_data/', include(router.urls)),
]
