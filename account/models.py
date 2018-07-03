from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Extends default Django User model to store information related to the User.

    The Profile model stores the data required to authenticate the user account.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    verified = models.NullBooleanField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    document_country_of_issue = models.CharField(max_length=100, blank=True,
                                                 null=True)
    document_series = models.IntegerField(blank=True, null=True)
    id_document_expiration_date = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    document_scan = models.ImageField(upload_to='users/%Y/%m/', blank=True)

    def __str__(self):
        return 'Account for user {}'.format(self.user.username)
