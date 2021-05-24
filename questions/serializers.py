from django.db import models
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Question, Option, Submission


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'sn',
            'title_en',
            'title_np',
            'choice_type',
            'options',
        ]


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = [
            'sn',
            'question',
            'title_en',
            'title_np',
        ]


class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            'user',
            'data',
        ]
