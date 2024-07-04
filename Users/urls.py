from django.urls import path
from . views import UserRegistrationApiView, activate,UserLoginApiView,UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', activate, name='activate'),
    path('login/', UserLoginApiView.as_view(), name='Login'),
    path('logout/', UserLogoutView.as_view(), name='Logout'),

]