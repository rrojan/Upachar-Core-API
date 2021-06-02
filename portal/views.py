from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import date
import math
from users.models import Profile
from questions.models import Submission


def index_view(request):

    counts = {
        'patients': Profile.objects.filter(user_type='patient').count(),
        'status_updates': Submission.objects.filter(date_added__startswith=date.today()).count(),
        'doctors': Profile.objects.filter(user_type='doctor').count(),
        'severe': len([elem for elem in Submission.objects.filter(date_added__startswith=date.today()) if elem.data['How is your condition (Mild/ Moderate/ Severe) in your understanding'].lower() == 'severe'])
    }

    SUB_DISPLAY = 10
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = Submission.objects.all().count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = Submission.objects.order_by('-date_added')[sub_start:sub_end]

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


def reports_today_view(request):

    counts = {
        'new_patients': User.objects.filter(date_joined__startswith=date.today()).count(),
        'status_updates': Submission.objects.filter(date_added__startswith=date.today()).count(),
        'severe': len([elem for elem in Submission.objects.filter(date_added__startswith=date.today()) if elem.data['How is your condition (Mild/ Moderate/ Severe) in your understanding'].lower() == 'severe'])
    }

    SUB_DISPLAY = 25
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = Submission.objects.all().count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = Submission.objects.order_by('-date_added')[sub_start:sub_end]

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


def reports_archive_view(request):

    counts = {
        'total': User.objects.all().count(),
        'patients': Profile.objects.filter(user_type='patient').count(),
        'status_updates': Submission.objects.all().count(),
        'doctors': Profile.objects.filter(user_type='doctor').count(),
    }

    SUB_DISPLAY = 50
    sub_start = int(request.GET.get('start')) if 'start' in request.GET else 0
    sub_end = int(request.GET.get('end')
                  ) if 'end' in request.GET else SUB_DISPLAY
    sub_total = Submission.objects.all().count()
    sub_pages = math.ceil(sub_total / SUB_DISPLAY)
    current_page = math.ceil(sub_end / SUB_DISPLAY)

    submissions = Submission.objects.order_by('-date_added')[sub_start:sub_end]

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
