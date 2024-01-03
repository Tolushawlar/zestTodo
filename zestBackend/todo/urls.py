from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import TodoItemListCreateView, TodoItemRetrieveUpdateDestroyView

urlpatterns = [
    path('item/', TodoItemListCreateView.as_view(), name='todo-list-create'),
    path('item/<int:pk>/',
         TodoItemRetrieveUpdateDestroyView.as_view(), name='todo-item-rud'),
]
