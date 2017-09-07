# -*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""
import django
from django.test import TestCase
from django.http.response import JsonResponse, HttpResponse
from .qrimage import generate,analysis
from app.models import PersonnelProfile

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)


def qrcode_generate(request):
    '''测试生成二维码'''
    try:
        pers = PersonnelProfile.objects.exclude(ID_number='').exclude(name='')
        for per in pers:
            data = {
                "uuid": per.personnel_uuid,
                "name": per.name,
                "ID_number": per.ID_number,
                "ID_photo": per.ID_photo
            }
            path_file = generate(data)
        return JsonResponse({"state": 200, "msg": "完成", "data": path_file})
    except Exception as e:
        return HttpResponse(e)

def qrcode_analysis(request):
    '''测试解析二维码'''
    try:
        data = analysis()
        return JsonResponse({"state": 200, "msg": "完成", "data": data})
    except Exception as e:
        return HttpResponse(e)