from django.urls import path, include
from questions import api_views as questions
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'questions', questions.QuestionList, basename="questions_list")
router.register(r'submit', questions.SubmissionViewSet, basename="submit")


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
