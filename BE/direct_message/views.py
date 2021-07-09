from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from direct_message.serializers import MessageSerializer
from rest_framework import response, status, generics, views
from direct_message.models import Message
from authentication.models import User
from rest_framework.response import Response
<<<<<<< HEAD

# Create your views here.


=======
from direct_message.serializers import MessageSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from authentication.serializers import RegisterSerializer

# Create your views here.

"""
>>>>>>> e1388b793271f23709b332851374932bef6ec486
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

<<<<<<< HEAD

=======
"""

def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:                                                                      # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id=pk)              # Select only that particular user
        else:
            users = User.objects.all()                             # Else get all user list
        serializer = RegisterSerializer(users, many=True, context={'request': request}) 
        return JsonResponse(serializer.data, safe=False)               # Return serialized data
    elif request.method == 'POST':
        data = JSONParser().parse(request)           # On POST, parse the request object to obtain the data in json
        serializer = RegisterSerializer(data=data)        # Seraialize the data
        if serializer.is_valid():
            serializer.save()                                            # Save it if valid
            return JsonResponse(serializer.data, status=201)     # Return back the data on success
        return JsonResponse(serializer.errors, status=400)     # Return back the errors  if not valid


def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
>>>>>>> e1388b793271f23709b332851374932bef6ec486
