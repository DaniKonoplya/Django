from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    my_context = {
        "my_text": 'This is about us',
        'this is true': True,
        'my_number': 123,
        'my_list': [123, 4343, 12345],
        'my_html': '<h2>Hello Denis</h2>'
    }
    return render(request, "home.html", my_context)


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")
