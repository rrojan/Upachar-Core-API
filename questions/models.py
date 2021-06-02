from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.http import JsonResponse
from django.forms.models import model_to_dict

CHOICE_TYPES = (
    ('s', 'Single-choice question'),
    ('m', 'Multiple-choice question')
)


class Question(models.Model):
    sn = models.IntegerField(unique=True)
    title_en = models.TextField()
    title_np = models.TextField(blank=True, null=True)
    choice_type = models.CharField(max_length=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def options(self):
        options_queryset = self.option_set.all()
        options_list = [{
            'sn': option.sn,
            'title_en': option.title_en,
            'title_np': option.title_np
        } for option in options_queryset]

        return options_list

    def __str__(self) -> str:
        return f'{self.title_en} [{self.title_np}]'


class Option(models.Model):
    sn = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title_en = models.TextField()
    title_np = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sn', 'question',)

    def __str__(self) -> str:
        return f'{self.title_en} [{self.title_np}]'


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    data = models.JSONField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
