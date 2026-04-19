from django.urls import path
from .views import process_ticket_view

urlpatterns = [
    path('process/', process_ticket_view),
]