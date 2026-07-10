from django.urls import path
from .views import DeliveryCreateView, DeliveryListCreateView, DeliveryDetailView, CreateUserView, ListUserView
urlpatterns = [
    path('create/', DeliveryCreateView.as_view(), name='create_delivery'),
    path('list/', DeliveryListCreateView.as_view(), name='list_delivery'),
    path('detail/<int:pk>/', DeliveryDetailView.as_view(), name='detail_delivery'),
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('list-users/', ListUserView.as_view(), name='list_users'),
]

