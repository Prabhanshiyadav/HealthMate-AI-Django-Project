from django.urls import path
from .views import (
    book_appointment,
    list_appointments,
    cancel_appointment,
    appointment_list,
)

urlpatterns = [
    path('list/', appointment_list, name='appointment_list'),
    path('book/', book_appointment, name='book_appointment'),
    path('list/', list_appointments, name='appointment_list'),
    path('cancel/<int:pk>/', cancel_appointment, name='cancel_appointment'),
]
