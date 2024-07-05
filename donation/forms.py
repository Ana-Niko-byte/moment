from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('full_name', 'charity', 'donation_amount', 'country', 'postcode',)

    def __init__(self, *args, **kwargs):
        '''
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name' : 'Mary Jane',
            'charity' : 'Please select a charity',
            'donation_amount' : '€5',
            'country' : 'Ireland',
            'postcode' : 'xxx xxxx',
        }

        # These don't fully work - check later - CI code.
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
