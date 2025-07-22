from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Home, About, Contact
    path('accounts/', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
    path('prescriptions/', include(('prescriptions.urls', 'prescriptions'), namespace='prescriptions')),  # ✅ namespaced
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
