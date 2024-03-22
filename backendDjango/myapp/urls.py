from myapp.views import process_csv_view
from django.urls import path

urlpatterns = [
    path('process-csv/', process_csv_view, name='process_csv'),  # Define a URL pattern
]
