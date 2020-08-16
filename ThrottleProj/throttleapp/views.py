# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework import status
from .models import UserModel, ActivityPeriodModel
from .serializers import UserSerializer, ActivityPeriodSerializer


# Create your views here.
class UsersList(APIView):
    def get(self, request):
        """
        This get method is used to fetch the data from the user,activity models and send the data in JSON format.
        :param request:
        :return:
        """
        all_users = UserModel.objects.all()
        users_serializer = UserSerializer(all_users, many=True)
        all_activity = ActivityPeriodModel.objects.all()
        activity_serializer = ActivityPeriodSerializer(all_activity, many=True)
        members_list = []
        total_list = {}
        for user in users_serializer.data:
            print(user)
            print(f"Count of Serializer : {len(users_serializer.data)}")
            activity_period = []
            for activity in activity_serializer.data:
                print(f"Activity :{activity}")
                if user['User_id'] == activity['User_id']:
                    activity_period.append({'start_time': activity['start_time'],
                                            'end_time': activity['end_time']})
            members_list.append({'id': user['User_id'], 'real_name': user['real_name'], 'tz': user['tz'],
                                 'activity_periods': activity_period})
            total_list['members'] = members_list
        # result_model = users_serializer.data + activity_serializer.data
        return Response(total_list)

    def post(self):
        pass


# methods to nest
class Usersapi(viewsets.ModelViewSet):
    """
    This class is used to crate a queryset for Users Model and initialize a serializer
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class ActivityPeriodapi(viewsets.ModelViewSet):
    """
    This class is used to crate a queryset for Activity Model and initialize a serializer
    """
    queryset = ActivityPeriodModel.objects.all()
    serializer_class = ActivityPeriodSerializer
