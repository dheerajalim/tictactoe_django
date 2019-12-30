from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name='invitations_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='invitations_received', on_delete=models.CASCADE,
                                verbose_name='User to Invite',
                                help_text='Please select user with whom you want to play')
    message = models.CharField(max_length=300,
                               blank=True,
                               verbose_name='Optional',
                               help_text='Add an invitation message'
                               )
    timestamp = models.DateTimeField(auto_now_add=True)