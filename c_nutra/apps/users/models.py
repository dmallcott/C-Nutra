from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # other fields here
    birthday = models.DateField(auto_now=True)
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Masculino'),
            ('F', 'Femenino')
        )
    )
    height = models.IntegerField()
    weight = models.IntegerField()
    elbow_diameter = models.IntegerField()

    def __unicode__(self):
        return u'Perfil de %s' % self.user

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = UserProfile.objects.get_or_create(user=instance)
