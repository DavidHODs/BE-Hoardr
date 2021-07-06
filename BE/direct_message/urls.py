from direct_message import views
from django.urls import path


urlpatterns=[
    path('/message', views.MessageAPIView.as_view(), name='message'),
]