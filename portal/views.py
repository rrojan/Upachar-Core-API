from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Profile
from questions.models import Submission


def index_view(request):

    counts = {
        'patients': Profile.objects.filter(user_type='patient').count(),
        'status_updates': 0,
        'severe': 0,
        'doctors': Profile.objects.filter(user_type='doctor').count(),
    }

    submissions = Submission.objects.order_by('date_added')[:10]


    context = {
        'counts': counts,
        'submissions': submissions,
    }
    return render(request, 'portal/index.html', context)
