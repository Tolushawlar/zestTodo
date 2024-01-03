from django.urls import path
from .views import UserRegistrationView, UserLoginView, UsersList

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('userslist/', UsersList.as_view(), name="userlist")
]
