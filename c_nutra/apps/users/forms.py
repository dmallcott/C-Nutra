from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserForm(forms.Form):
    username = forms.CharField(required=False)
    email = forms.EmailField(
        required=False,
        error_messages={
            'invalid': u'Formato incorrecto de email.'
        }
    )
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)


class UserProfileForm(forms.Form):
    birthday = forms.DateField(
        required=False,
        input_formats=["%d-%m-%Y"],
        error_messages={
            'invalid': u'El formato de la fecha es dd-mm-yyyy.'
        }
    )
    gender = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=(
                            ('M', 'Masculino'),
                            ('F', 'Femenino')
            )
        )
    )
    height = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            'invalid': u'Esto no pasa con html5.',
            'min_value': u'La altura no puede ser negativa.'
        }
    )
    weight = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            'invalid': u'Esto no pasa con html5.',
            'min_value': u'El peso no puede ser negativo.'
        }
    )
    elbow_diameter = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            'invalid': u'Esto no pasa con html5.',
            'min_value': u'El diametro del codo no puede ser negativo.'
        }
    )
