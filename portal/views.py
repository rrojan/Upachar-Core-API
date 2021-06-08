from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date
import math
from users.models import Profile
from questions.models import Submission


# TODO: refactor to clean up repeated code

@login_required
def index_view(request):
    # reduce number of db reads:
    profiles = Profile.objects.filter(hospital_name=request.user.username)
    submissions = Submission.objects.filter(
        user__profile__hospital_name=request.user.username)

    counts = {
        'patients': profiles.filter(user_type='patient').count(),
        'status_updates': submissions.filter(date_added__startswith=date.today()).count(),
        'doctors': profiles.filter(user_type='doctor').count(),
        'severe': len([elem for elem in submissions.filter(date_added__startswith=date.today()) if elem.data['How is your condition (Mild/ Moderate/ Severe) in your understanding'].lower() == 'severe'])
    }

    SUB_DISPLAY = 10
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = submissions.count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = submissions.order_by('-date_added')[sub_start:sub_end]

    context = {
        'page': 'dashboard',
        'counts': counts,
        'submissions': submissions,
        'sub_start': sub_start + 1,
        'sub_end': sub_end if sub_end < sub_total else sub_total,
        'sub_pages': sub_pages,
        'sub_total': sub_total,
        'sub_range': range(1, sub_pages + 1),
        'current_page': current_page
    }
    return render(request, 'portal/index.html', context)


@login_required
def reports_today_view(request):

    profiles = Profile.objects.filter(hospital_name=request.user.username)
    submissions = Submission.objects.filter(
        user__profile__hospital_name=request.user.username)

    counts = {
        'new_patients': profiles.filter(user__date_joined__startswith=date.today()).count(),
        'status_updates': submissions.filter(date_added__startswith=date.today()).count(),
        'severe': len([elem for elem in submissions.filter(date_added__startswith=date.today()) if elem.data['How is your condition (Mild/ Moderate/ Severe) in your understanding'].lower() == 'severe'])
    }

    SUB_DISPLAY = 25
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = submissions.all().count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = submissions.order_by('-date_added')[sub_start:sub_end]

    context = {
        'page': 'today',
        'counts': counts,
        'submissions': submissions,
        'sub_start': sub_start + 1,
        'sub_end': sub_end if sub_end < sub_total else sub_total,
        'sub_pages': sub_pages,
        'sub_total': sub_total,
        'sub_range': range(1, sub_pages + 1),
        'current_page': current_page
    }
    return render(request, 'portal/reports_today.html', context)


@login_required
def reports_archive_view(request):

    profiles = Profile.objects.filter(hospital_name=request.user.username)
    submissions = Submission.objects.filter(
        user__profile__hospital_name=request.user.username)

    counts = {
        'total': profiles.count(),
        'patients': profiles.filter(user_type='patient').count(),
        'status_updates': submissions.all().count(),
        'doctors': profiles.filter(user_type='doctor').count(),
    }

    SUB_DISPLAY = 50
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = submissions.all().count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = submissions.order_by('-date_added')[sub_start:sub_end]

    context = {
        'page': 'archive',
        'counts': counts,
        'submissions': submissions,
        'sub_start': sub_start + 1,
        'sub_end': sub_end if sub_end < sub_total else sub_total,
        'sub_pages': sub_pages,
        'sub_total': sub_total,
        'sub_range': range(1, sub_pages + 1),
        'current_page': current_page
    }
    return render(request, 'portal/reports_archive.html', context)



@login_required
def all_patients_view(request):

    profiles = Profile.objects.filter(hospital_name=request.user.username).order_by('name')
    patients = profiles.filter(user_type='patient')
    submissions = Submission.objects.filter(
        user__profile__hospital_name=request.user.username)

    counts = {
        'total': profiles.count() - 1,
        'patients': patients.count(),
        'status_updates': submissions.count(),
    }

    SUB_DISPLAY = 25
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = profiles.count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = submissions.order_by('-date_added')[sub_start:sub_end]

    context = {
        'page': 'all_patients',
        'counts': counts,
        'patients': patients,
        'sub_start': sub_start + 1,
        'sub_end': sub_end if sub_end < sub_total else sub_total,
        'sub_pages': sub_pages,
        'sub_total': sub_total,
        'sub_range': range(1, sub_pages + 1),
        'current_page': current_page
    }
    return render(request, 'portal/patients_all.html', context)



@login_required
def all_doctors_view(request):

    profiles = Profile.objects.filter(hospital_name=request.user.username).order_by('name')
    patients = profiles.filter(user_type='patient')
    doctors = profiles.filter(user_type='doctor')

    counts = {
        'total': profiles.count() - 1,
        'patients': patients.count(),
        'doctors': doctors.count(),
    }

    SUB_DISPLAY = 10
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = profiles.count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    context = {
        'page': 'all_doctors',
        'counts': counts,
        'doctors': doctors,

        'sub_start': sub_start + 1,
        'sub_end': sub_end if sub_end < sub_total else sub_total,
        'sub_pages': sub_pages,
        'sub_total': sub_total,
        'sub_range': range(1, sub_pages + 1),
        'current_page': current_page
    }
    return render(request, 'portal/doctors_all.html', context)


def report_detail_view(request, pk):
    context = {
        'page': 'archive',
        'report': Submission.objects.get(pk=pk),
    }
    return render(request, 'portal/report_detail.html', context)