from rest_framework import serializers
from direct_message.models import Message
<<<<<<< HEAD
<<<<<<< HEAD
=======
from authentication.models import User
>>>>>>> e1388b793271f23709b332851374932bef6ec486
=======
from authentication.models import User
>>>>>>> e1388b793271f23709b332851374932bef6ec486


class MessageSerializer(serializers.ModelSerializer):

<<<<<<< HEAD
<<<<<<< HEAD
    class Meta:
        model = Message
        fields = ('user', 'sender', 'recipient', 'body', 'date', 'is_read')
=======
=======
>>>>>>> e1388b793271f23709b332851374932bef6ec486
    sender = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ('user', 'sender', 'receiver',  'recipient', 'body', 'date', 'is_read')
<<<<<<< HEAD
>>>>>>> e1388b793271f23709b332851374932bef6ec486
=======
>>>>>>> e1388b793271f23709b332851374932bef6ec486

        read_only_fields = ['date', 'is_read']