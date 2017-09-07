"""
Definition of urls for xj.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.tests
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
    url(r'^api/qrcode', app.tests.qrcode_generate),
    url(r'^api/analysis', app.tests.qrcode_analysis),
    url(r'^api/face/recognition', app.api.face_recognition),

    #mobile url
    url(r'^personnel/detail/(?P<pid>.+)$', app.personnel.get_detail, name='get_detail'),

    # web url
    url(r'^$', app.views.home, name='home'),
    url(r'^users', app.views.user_index, name='users'),
    url(r'^user/add', app.views.user_add, name='user_add'),
    url(r'^user/save', app.views.user_save, name='user_save'),
    url(r'^user/delete/(?P<id>\d+)', app.views.user_delete, name='user_delete'),
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
    url(r'^data/import', app.admin.import_data, name='import_data'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

]
