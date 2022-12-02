from rest_framework import serializers
from polls.models import Question
from polls.models import Choice

class ChoicesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['question','choice_text','votes']


class QuestionModelSerializer(serializers.ModelSerializer):
    choices = ChoicesModelSerializer(many=True)
    class Meta:
        model = Question
        fields = ["id","question_text","pub_date","choices"]

    