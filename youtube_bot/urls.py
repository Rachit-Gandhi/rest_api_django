from django.urls import path
from .views import get_subtitle_text

urlpatterns = [
    path('get_subtitle_text/', get_subtitle_text, name='get_subtitle_text'),
]
