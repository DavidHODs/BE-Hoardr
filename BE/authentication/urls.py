from authentication import views
from django.urls import path


urlpatterns=[
    path('/signup', views.RegisterAPIView.as_view(), name='signup'),
    path('/login', views.LoginAPIVIEW.as_view(), name='login'),
    path('/logout', views.LogoutAPIView.as_view(), name='logout'),
    path('/change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]