from rest_framework import viewsets
from .models import Question, Choice
from .serializers import QuestionModelSerializer, ChoicesModelSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class = QuestionModelSerializer
    permission_classes = []

class ChoicesViewSet(viewsets.ModelViewSet):
    queryset= Choice.objects.all()
    serializer_class = ChoicesModelSerializer
    permission_classes = []