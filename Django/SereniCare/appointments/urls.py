from django.urls import path
from .views import (
    book_appointment,
    list_appointments,
    cancel_appointment
)

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path('list/', list_appointments, name='appointment_list'),
    path('cancel/<int:pk>/', cancel_appointment, name='cancel_appointment'),
]
