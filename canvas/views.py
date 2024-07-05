from django.shortcuts import render


def canvas(request):
    return render(
        request,
        'canvas/canvas.html'
    )