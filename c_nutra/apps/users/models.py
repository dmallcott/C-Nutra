# -*- coding: utf-8 -*-
from __future__ import division
from django.db import models
from django.contrib.auth.models import User
from datetime import date


# User Profile Model

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        # name="Usuario",
        verbose_name="the user who's profile this is"
    )
    birthday = models.DateField(
        # name="Cumpleanos",
        verbose_name='the date of birth',
        auto_now=False
    )
    gender = models.CharField(
        # name="Genero",
        verbose_name="the user's gender",
        max_length=1,
        choices=(
            ('M', 'Masculino'),
            ('F', 'Femenino')
        )
    )
    height = models.IntegerField(
        # name="Altura",
        verbose_name="the user's height"
    )
    weight = models.IntegerField(
        # name="Peso",
        verbose_name="the user's weight"
    )
    elbow_diameter = models.IntegerField(
        #name="Diametro del codo",
        verbose_name="the user's elbow diameter"
    )
    activity_level = models.CharField(
        #name="Nivel de actividad",
        verbose_name="the user's activity levels",
        max_length=2,
        choices=(
            ('EN', 'Sedentario'),
            ('EL', 'Ejercicio ligero'),
            ('EM', 'Ejercicio moderado'),
            ('EF', 'Ejercicio fuerte'),
            ('EE', 'Ejercicio extreno')
        )
    )

    class Meta:
        verbose_name = ('Perfil')
        verbose_name_plural = ('Perfiles')

    def __str__(self):
        return 'Perfil de %s' % self.user

    # Will be deprecated with django-registration
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = UserProfile.objects.get_or_create(user=instance)

    # Given the date of birth it calculates the age
    def calculate_age(self):
        today = date.today()
        born = self.birthday
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    # Given the user's height and weight it calculates the body mass index
    def calculate_bmi(self):
        height = self.height / 100  # Height must be in meters
        weight = self.weight
        # Result is rounded up to one decimal
        return "%.1f" % float(weight / height ** 2)

    # Given the user's height and weight it calculates the daily energy
    # expenditure (calories)
    def calculate_dem(self):
        # First the basal metamolic rate must be obtained
        # The Mifflin St Jeor Equation will be used for this
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.calculate_age()

        if self.gender == 'F':
            bmr -= 161
        else:
            bmr += 5
        # Afterwards the Harris-Benedict Principle is applied
        if self.activity_level == 'EN':
            dem = 1.2 * bmr
        elif self.activity_level == 'EL':
            dem = 1.375 * bmr
        elif self.activity_level == 'EM':
            dem = 1.55 * bmr
        elif self.activity_level == 'EF':
            dem = 1.725 * bmr
        elif self.activity_level == 'EE':
            dem = 1.9 * bmr
        else:
            # TO-DO: raise an exception here
            dem = -1
        # Result is rounded up to an integer
        return int(dem)
