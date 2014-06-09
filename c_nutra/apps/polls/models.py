from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
	user = models.ForeignKey(User)

class BodyMassIndex(Poll):
	bmi = models.IntegerField()