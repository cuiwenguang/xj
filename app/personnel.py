# -*- coding:utf-8 -*-
from app.models import *
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="/login/")
@csrf_exempt
def get_profile(request, pid):
    family_master = None
    family_members = []
    per = PersonnelProfile.objects.get(personnel_uuid=pid)
    if per is not None:
        family_ids = Family.objects.filter(family_master_uuid=pid).values_list('personnel_uuid')
        family_pers = PersonnelProfile.objects.filter(personnel_uuid__in=family_ids)
        if len(family_pers) == 0:
            family_per = Family.objects.get(personnel_uuid=pid)
            if family_per is not None:
                family_ids = Family.objects.filter(family_master_uuid=family_per.family_master_uuid).values_list('personnel_uuid')
                family_pers = PersonnelProfile.objects.filter(personnel_uuid__in=family_ids)
                family_master = PersonnelProfile.objects.get(personnel_uuid=family_per.family_master_uuid)
        else:
            family_master = per

        for fper in family_pers:
            family = Family.objects.get(personnel_uuid=fper.personnel_uuid)
            family_members.append({"name": fper.name,
                                   "ID_number": fper.ID_number,
                                   "nation": fper.nation,
                                   "educational_level": fper.educational_level,
                                   "political_face": fper.political_face,
                                   "marriage": fper.marriage,
                                   "health": fper.health,
                                   "note": fper.note,
                                   "phone_number": fper.phone_number,
                                   "work_source": fper.work_source,
                                   "work_desc": fper.work_desc,
                                   "family_relation": family.family_relation})

    context = {'family_master': family_master, 'family_members': family_members}
    return render(request, 'app/personneldetail.html', context)
