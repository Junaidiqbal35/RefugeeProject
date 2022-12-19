from django.urls import path
from . import views

urlpatterns = [
    # path('create/', views.accommodation_create, name='create-accommodation')
    path('', views.AccommodationList.as_view(), name='home'),
    path('create/', views.CreateAccommodationView.as_view(), name='create_accommodation'),
    path('accommodation/<int:pk>/', views.AccommodationDetailView.as_view(), name='detail_accommodation'),
]
