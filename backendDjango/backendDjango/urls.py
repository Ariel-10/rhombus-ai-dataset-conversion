from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  # This line includes the admin site URLs. It maps any URLs that start with "admin/" to Django's built-in admin interface.
    path('myapp/', include('myapp.urls')),  # This line includes URLs from the 'myapp' application. It tells Django to look for a `urls.py` file in the 'myapp' application directory and include those URLs, prefixing them with 'myapp/'.
]
