from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def charity(request):
    return render(
        request,
        "charity/index.html"
    )
