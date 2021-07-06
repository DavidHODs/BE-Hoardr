from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from direct_message.serializers import MessageSerializer
from rest_framework import response, status, generics, views
from direct_message.models import Message
from rest_framework.response import Response

# Create your views here.


class MessageAPIView(GenericAPIView):

	serializer_class = MessageSerializer
	queryset = Message.objects.all()
	model = Message
	lookup_field = 'id'

	def post(self, request):
		user = request.data
		serializer = self.serializer_class(data=user)

		if serializer.is_valid():
			serializer.save()

			return response.Response(serializer.data, status=status.HTTP_200_OK)
		return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)