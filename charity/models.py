from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.utils.text import slugify

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
    '''
    Represents a Charity (model).

    Attributes:
    name : CharField - the Charity name.
    slug : SlugField - the charity slug (slugified name field).
    description : TextField - the Charity description.
    entry_donation : DecimalField - the minimum donation amount.
    category : CharField (selectionfield) - the Charity organisation category.
    community_size : IntegerField - non-editable, the size of the charity
    community (number of donatees).
    donated_to_by : ManyToManyField - non-editable, users who have donated to
    the charity.
    image : CloudinaryField - the charity banner image.
    approved : BooleanField - administration approval.

    Meta:
    Orders by community size (largest to smallest).

    Returns:
    (str) : 'Charity: "(name)" - "(category)". Size: (community size)'.
    '''
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(max_length=300)
    entry_donation = models.DecimalField(
        decimal_places=2,
        validators=[
            MinValueValidator(
                0.01,
                message='Please ensure min donation is greater than €0.01'
            ),
        ],
        max_digits=5,
        help_text='The min donation required to enter the charity community.'
    )
    category = models.CharField(
        max_length=25,
        choices=CATEGORIES,
        default='Other'
    )
    community_size = models.IntegerField(default=0, editable=False)
    donated_to_by = models.ManyToManyField(
        User,
        related_name='donated_user',
        blank=True,
        editable=False
    )
    image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-community_size']

    def __str__(self):
        '''
        Returns:
        (str) : a user-friendly string in the admin panel.
        '''
        return f'''Charity: "{self.name}" - "{self.category}".
        Size: {self.community_size}'''

    def save(self, *args, **kwargs):
        '''
        Ensures the slug updates following a name change in the charity model.

        Method:
        Asserts whether the stored database charity name matches the instance
        Charity name with the same id.
        If the names do not match, regenerates (slugifies) the name and
        saves the model.
        '''
        try:
            if self.name != Charity.objects.get(id=self.id).name:
                self.slug = slugify(self.name)
            super(Charity, self).save(*args, **kwargs)
        # Adding new charity via form threw DoesotExist error.
        # Wrapping in try except + saving navigates this issue.
        except Charity.DoesNotExist:
            super(Charity, self).save(*args, **kwargs)


class Product(models.Model):
    # Will be designed after main functionality has been incorporated
    '''
    Represents a Product (model). This is the end product of a finished
    community canvas.

    Attributes:

    Meta:

    Returns:
    '''


class Profile(models.Model):
    '''
    Represents a user Profile (model).

    Attributes:
    user : OneToOneField - a direct relationship with Django's User model.
    birth_date : DateField - the user's birth date.
    charities : ManyToManyField - a list of charities the user has donated to.
    date_added : DateField - the date the user created their profile.

    Returns:
    (str) : 'Profile for user: (user)'
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    charities = models.ManyToManyField(
        Charity,
        related_name='user_charities',
        blank=True,
        editable=False
    )
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Profile for user: {self.user}'
