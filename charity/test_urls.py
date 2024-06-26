from django.test import TestCase
from django.urls import resolve, reverse
from charity.urls import *

class TestCharityURLs(TestCase):
    '''
    A class for testing URLs associated with Charity Views.

    Methods:
    def test_charity_home_resolves():
        Reverses the URL name and checks if it returns the correct
        FBV of charity.
        Asserts charity is resolved from 'home'.
    '''
    def test_charity_home_resolves(self):
        path = reverse('home')
        self.assertEqual(resolve(path).func, charity)