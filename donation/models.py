from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.conf import settings

from charity.models import Charity

import uuid

# Create your models here.
class Donation(models.Model):
    '''
    Represents a Donation (model) with basic information.

    Attributes:
    donatee : FK : User - the user who made the donation.
    charity : FK : Charity - the charity to which the donation was made.
    amount : DecimalField - the amount to be donated.
    donation_date : DateField - the date on which the donation was made.

    Meta:
    Orders by donation date (latest to later).

    Returns:
    (str) : '(amount) donated to "(charity)" by (user)'.
    '''
    donation_number = models.CharField(max_length=32, null=False, editable=False)
    donation_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='donation_user'
    )
    charity = models.ForeignKey(
        Charity,
        on_delete=models.CASCADE,
        related_name='charity_donation'
    )
    donation_amount = models.DecimalField(
        decimal_places=2,
        validators=[
            MinValueValidator(
                0.01,
                message='Please ensure min donation is greater than €0.01'
            ),
        ],
        max_digits=5,
        help_text='The donation made by the user.'
    )
    donation_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-donation_date']

    def __str__(self):
        return f'{self.amount} donated to "{self.charity}" by {self.user}'

    def _generate_donation_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super(Donation, self).save(*args, **kwargs)