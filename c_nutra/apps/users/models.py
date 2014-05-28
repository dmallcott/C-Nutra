from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import date

class UserProfile(models.Model):
	user = models.OneToOneField(User)  
	#other fields here
	birthday = models.DateField(default=date.today)
	gender = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
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

class UserProfileForm(forms.Form):
	birthday = forms.DateField(required=False, input_formats=["%d-%m-%Y"], 
		error_messages={'required': u'Este campo es requerido', 'invalid': u'El formato de la fecha es dd-mm-yyyy'})
	gender = forms.CharField(required=False, widget=forms.Select(choices=(('M', 'Masculino'), ('F', 'Femenino'))))
	height = forms.IntegerField(required=False)
	weight = forms.IntegerField(required=False)
	elbow_diameter = forms.IntegerField(required=False)
