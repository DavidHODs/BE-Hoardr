from authentication import views
from django.urls import path


urlpatterns=[
    path('/signup', views.RegisterAPIView.as_view(), name='signup'),
    path('/email-verification', views.VerifyEmail.as_view(), name='email-verification'),
    path('/login', views.LoginAPIView.as_view(), name='login'),
    path('/profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('/logout', views.LogoutAPIView.as_view(), name='logout'),
    path('/change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]