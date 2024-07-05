from django.db import models
from django.db.models import Count
from charity.models import Charity
from django.contrib.auth.models import User


class Canvas(models.Model):
    '''
    Represents a Canvas (model).

    Attributes:
    canvas_name : CharField - the Canvas name.
    charity : FK : Charity - the charity to which the canvas belongs.
    contributors : ManyToManyField : User - the users who have contributed to the canvas.
    start_date : DateField - the date the canvas was created on.
    due_date : DateField - the date the canvas is due on.

    Meta:
    Orders by latest created.

    Returns:
    (str) : '(Canvas Name), contributors: (number of contributors)'.
    '''
    canvas_name = models.CharField(max_length=100)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='charity_canvas')
    contributors = models.ManyToManyField(User, blank=True)
    start_date = models.DateField()
    due_date = models.DateField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.canvas_name}, contributors: {self.contributors_count}'

    def return_contributors_count(self):
        '''
        Returns the number of contributors for each canvas.
        '''
        self.contributors_count = self.contributors.count()
        return contributors_count