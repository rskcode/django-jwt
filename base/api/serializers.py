from rest_framework.serializers import ModelSerializer
from base.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'body']