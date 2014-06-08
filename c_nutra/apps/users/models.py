from django.db import models
from django.contrib.auth.models import User

# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="the user who's profile this is")
    birthday = models.DateField(auto_now=True, verbose_name='the date of birth')
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Masculino'),
            ('F', 'Femenino')
        ),
        verbose_name="the user's gender"
    )
    height = models.IntegerField(verbose_name="the user's height")
    weight = models.IntegerField(verbose_name="the user's weight")
    elbow_diameter = models.IntegerField(verbose_name="the user's elbow diameter")

    def __unicode__(self):
        return u'Perfil de %s' % self.user

    # Will be deprecated with django-registration
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = UserProfile.objects.get_or_create(user=instance)
