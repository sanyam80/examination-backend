
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('student.urls')),
    path('api/', include('staff.urls')),
    path('api/', include('exam.urls')),
    path('api/', include('exam.urls'))
]
