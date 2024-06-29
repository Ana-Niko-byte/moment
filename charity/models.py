from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

CATEGORIES = (
    ('Animal', 'Animal Welfare'),
    ('Children', 'Children & Youth'),
    ('Conservation', 'Conservation'),
    ('Disaster', 'Disaster Relief'),
    ('Education', 'Education'),
    ('Environment', 'Environment'),
    ('Homelessness', 'Homelessness'),
    ('Humanitarian', 'Humanitarian Aid'),
    ('Medical', 'Medical Research'),
    ('Sustainability', 'Sustainable Development'),
    ('Other', 'Other'),
)


class Charity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(max_length=300)
    entry_donation = models.DecimalField(
        decimal_places=2,
        validators=[
            MinValueValidator(
                0.01,
                message='Ensure min donation is greater than €0.01'
            ),
        ],
        max_digits=5,
        help_text='The min donation required to enter the charity community.'
    )
    category = models.CharField(max_length=25, choices=CATEGORIES, default='Other')
    image = CloudinaryField('image', default='placeholder')
