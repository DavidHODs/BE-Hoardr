from rest_framework import serializers
from direct_message.models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('user', 'sender', 'recipient', 'body', 'date', 'is_read')

        read_only_fields = ['date', 'is_read']