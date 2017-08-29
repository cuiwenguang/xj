"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


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

@csrf_exempt
def user_save(request):
    username = request.POST['username']
    email = "xj_" + username + "@admin.com"
    password = request.POST['password']
    if User.objects.filter(Q(email=email) | Q(username=username)).exists():
        msg ={
            "state": 201,
            "msg": "用户已存在", }
    else:
        user = User.objects.create_user(username, email=email, password=password)
    return HttpResponseRedirect(reverse(user_index))

def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse(user_index))
