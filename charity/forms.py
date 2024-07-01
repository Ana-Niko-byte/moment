from django import forms


SUBJECTS = (
    ('G', 'General Enquiry'),
    ('CS', 'Customer Support'),
    ('TN', 'Technical Support'),
    ('BP', 'Billing & Payments'),
    ('CO', 'Career Opportunities'),
    ('C', 'Complaint'),
    ('O', 'Other'),
)

class ContactForm(forms.Form):
    """
    
    """
    name = forms.CharField(
        label='Your Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'Mary Jane'}
        )
    )
    email = forms.EmailField(
        label='Your Email Address',
        widget=forms.TextInput(
            attrs={'placeholder': 'mariajane@example.com'}
        )
    )
    subject = forms.ChoiceField(
        label='Subject',
        choices=SUBJECTS,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    message = forms.CharField(
        label='Your Message (max 400 characters)',
        max_length=400,
        widget=forms.Textarea(
            attrs={'placeholder': 'Please tell us your query...'}
        )
    )