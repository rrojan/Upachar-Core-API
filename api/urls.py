from django.urls import path, include
from questions import api_views as questions
from rest_framework.routers import SimpleRouter
# from rest_framework.authtoken import views as authtoken
from users import api_views as users


router = SimpleRouter()
router.register(r'questions', questions.QuestionList,
                basename="questions_list")
router.register(r'submit', questions.SubmissionViewSet, basename="submit")


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('get-token/', questions.CustomAuthToken.as_view(), name='get_token'),
    path('register/', users.Register.as_view(), name='register'),
    path('', include(router.urls)),
]
