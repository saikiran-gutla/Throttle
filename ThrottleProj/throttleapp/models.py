from django.db import models


# Create your models here.
class UserModel(models.Model):
    User_id = models.CharField(max_length=50, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return str(self.real_name) or ""


# Create your models here.
class ActivityPeriodModel(models.Model):
    User_id = models.ForeignKey(UserModel, related_name='Activity', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'ActivityPeriods'

    def __str__(self):
        return str(self.User_id) or ""
