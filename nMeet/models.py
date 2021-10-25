#Model definitions
from django.db import models
from django_timestamps.timestamps import TimestampsModel
#Note branch fields in dashboard and chat tables are intentionally not implemented as foreign keys.
#This is because the application is very small and these tables are cleared at the end of the meeting.
#Thus, they will not put immense strain on the db or affect performance.
class Dashboard(TimestampsModel,models.Model):
	branch = models.CharField(max_length=20)
	teller_or_operator = models.CharField(max_length=15)
	debit = models.CharField(max_length=20)
	credit = models.CharField(max_length=20)
	updated = models.BooleanField(default=False)
class Chat(TimestampsModel,models.Model):
	branch = models.CharField(max_length=20)
	text = models.CharField(max_length=200)
class Cancelled(models.Model):
	id_of_cancelled_fig = models.BigIntegerField(blank=False,null=False)