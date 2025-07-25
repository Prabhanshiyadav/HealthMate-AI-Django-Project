from django.urls import include, path
from .views import home_view, about_view, contact_view, view_prescriptions

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('prescriptions/', include('prescriptions.urls', namespace='prescriptions')),

]
