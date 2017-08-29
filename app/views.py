"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User, Group

def home(request):
    """Renders the home page."""

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def mobile_detail(request):
    return render(
        request,
        "app/m_detail.html"
    )

def user_index(request):
    users = User.objects.all().exclude(username='admin')
    context = {'users': users}
    return render(request, 'app/userlist.html', context)

def user_add(request):
    return render(request, 'app/useradd.html')

def user_save(request):

    return render(request, 'app/userlist.html')
