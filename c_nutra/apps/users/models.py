from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserProfile(models.Model):  

	user = models.OneToOneField(User)  
	#other fields here
	age = models.IntegerField()
	gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
	height = models.IntegerField()
	weight = models.IntegerField()
	elbow_diameter = models.IntegerField()

	def __str__(self):  
		return "%s's profile" % self.user  

	def create_user_profile(sender, instance, created, **kwargs):  
		if created:  
			profile, created = UserProfile.objects.get_or_create(user=instance)  

class UserForm(forms.ModelForm):
	class Meta:
		model = User  

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user']