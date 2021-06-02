from django.urls import path, include
from rest_framework.routers import SimpleRouter
from questions import api_views as questions
from users import api_views as users


router = SimpleRouter()
router.register(r'questions', questions.QuestionList,
                basename="questions_list")
router.register(r'submit', questions.SubmissionViewSet, basename="submit")
router.register(r'hospitals', users.HospitalChoices, basename="hospitals")


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('get-token/', questions.CustomAuthToken.as_view(), name='get_token'),
    path('register/', users.Register.as_view(), name='register'),
    path('', include(router.urls)),
]
