from rest_framework import serializers

from student.models import MentalMessages


class MentalMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalMessages
        fields = '__all__'
