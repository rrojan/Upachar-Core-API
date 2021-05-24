from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from datetime import date
from .serializers import QuestionSerializer, SubmissionSerializer
from .models import Question, Submission
from rest_framework.permissions import IsAuthenticated


class QuestionList(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Question.objects.order_by("sn")
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class SubmissionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self, request):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                Submission.objects.get(date_added__startswith=date.today(), user=request.user)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
