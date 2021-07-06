from django.shortcuts import render
from rest_framework.generics import GenericAPIView, UpdateAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, ChangePasswordSerializer, EmailVerificationSerializer
from rest_framework import response, status, generics, views
from authentication.models import User, Profile
from django.contrib.auth import authenticate, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from . import serializers
from rest_framework.permissions import IsAuthenticated
from authentication.models import User, Profile
from authentication.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class RegisterAPIView(GenericAPIView):
    
    serializer_class = RegisterSerializer

    def post(self, request):

    	user = request.data
    	serializer = self.serializer_class(data=user)
    	# serializer = self.serializer_class(data=request.data)

    	if serializer.is_valid():
    		serializer.save()
    		user_data = serializer.data

            # commenting this part out till we set up the app email...

    		# user =User.objects.get(email=user_data['email'])
    		# token = RefreshToken.for_user(user).access_token

    		# current_site = get_current_site(request).domain
    		# relative_link = reverse('email-verification')
    		# absurl = 'http://'+current_site+relative_link+'?token='+str(token)
    		# email_body = 'Hi '+user.first_name+', use the this link to verify your email. \n'+absurl
    		# data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

    		# Util.send_email(data)

    		return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    	return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(views.APIView):

	serializer_class = EmailVerificationSerializer
	token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

	@swagger_auto_schema(manual_parameters=[token_param_config])
	def get(self, request):

		token = request.GET.get('token')

		try:
			payload = jwt.decode(token, settings.SECRET_KEY)
			user = User.objects.get(id=payload['id'])

			if not user.email_verified:

				user.email_verified = True
				user.save()

			return response.Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)

		except jwt.ExpiredSignatureError as identifier:
			return response.Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)

		except jwt.exceptions.DecodeError as identifier:
			return response.Response({'error': 'Invalid token. Request for a new one'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

	queryset = User.objects.all()
	# permission_classes = (IsAuthenticated,)
	serializer_class = LoginSerializer

	def post(self, request):
	    email = request.data.get('email', None)
	    password = request.data.get('password', None)

	    user = authenticate(username=email, password=password)

	    if user:
	        serializer = self.serializer_class(user)

	        return response.Response(serializer.data, status=status.HTTP_200_OK)
	    return response.Response({'message':'Invalid Credentials!! Try Again..'}, status=status.HTTP_401_UNAUTHORIZED)



class ProfileView(UpdateAPIView):

    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    lookup_field = ('id')



class LogoutAPIView(APIView):
    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"success": ("Successfully logged out.")},
                        status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):      
        
        model = User
        serializer_class = ChangePasswordSerializer
        # permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)