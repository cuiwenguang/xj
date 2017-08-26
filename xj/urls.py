"""
Definition of urls for xj.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.api
import app.views
import app.personnel
import app.admin
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # api url
    url(r'^api/signup',app.api.sign_up),
    url(r'^api/signin',app.api.sign_in),
    url(r'^api/signout', app.api.sign_out),
    url(r'^api/qrcode', app.api.qrcode_generate),
    url(r'^api/analysis', app.api.qrcode_analysis),
    #mobile url
    url(r'mobile/detail', app.views.mobile_detail, name="mobile_detail"),

    # web url
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^users', app.views.user_index, name='users'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^personnel/detail/(?P<pid>.+)$', app.personnel.get_detail, name='get_detail'),
    url(r'^data/import', app.admin.import_data, name='import_data'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

]
