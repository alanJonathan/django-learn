from rest_framework import routers
from polls.views import QuestionViewSet, ChoicesViewSet

router= routers.DefaultRouter()

router.register('polls/questions', QuestionViewSet, basename='questions')
router.register('polls/choices', ChoicesViewSet, basename='choices')
