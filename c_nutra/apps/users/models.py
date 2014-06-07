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

class UserForm(forms.Form):
	username = forms.CharField(required=False)
	email = forms.EmailField(required=False,
		error_messages={'invalid': u'Formato incorrecto de email.'})
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)


class UserProfileForm(forms.Form):
	birthday = forms.DateField(required=False, input_formats=["%d-%m-%Y"], 
		error_messages={'invalid': u'El formato de la fecha es dd-mm-yyyy.'})
	gender = forms.CharField(required=False, widget=forms.Select(choices=(('M', 'Masculino'), ('F', 'Femenino'))))
	height = forms.IntegerField(required=False, min_value=1,
		error_messages={'invalid': u'Esto no pasa con html5.', 'min_value': u'La altura no puede ser negativa.'})
	weight = forms.IntegerField(required=False, min_value=1,
		error_messages={'invalid': u'Esto no pasa con html5.', 'min_value': u'El peso no puede ser negativo.'})
	elbow_diameter = forms.IntegerField(required=False, min_value=1,
		error_messages={'invalid': u'Esto no pasa con html5.', 'min_value': u'El diametro del codo no puede ser negativo.'})
