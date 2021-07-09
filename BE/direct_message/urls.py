<<<<<<< HEAD
from direct_message import views
from django.urls import path


urlpatterns=[
    path('/message', views.MessageAPIView.as_view(), name='message'),
]

=======
from . import views
from django.urls import path

"""
urlpatterns=[
    path('/message', views.MessageAPIView.as_view(), name='message'),
]
"""
urlpatterns = [
    # URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list, name='message-list'),   # For POST

    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
]
>>>>>>> e1388b793271f23709b332851374932bef6ec486
