from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.accommodation_create, name='create_accommodation'),
    path('', views.accommodation_list, name='home'),
    # path('create/', views.CreateAccommodationView.as_view(), name='create_accommodation'),
    path('accommodation/<int:pk>/', views.accommodation_detail, name='detail_accommodation'),
    path('accommodation/search/', views.accommodation_search, name='accommodation_search'),
    path('accommodation/<int:pk>/booking/', views.booking_accommodation, name='booking'),
    path('accommodation/update/<int:pk>/', views.edit_accommodation, name='update_accommodation'),
    path('user-booking/request/', views.user_sending_booking_request, name='user_booking_page')

]
