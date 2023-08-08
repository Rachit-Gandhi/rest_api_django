from django.urls import path
from youtube_bot.views import get_subtitle_text, render_home_page


urlpatterns = [
    path('get_subtitle_text/', get_subtitle_text, name='get_subtitle_text'),
    path('home/', render_home_page, name="index")
]
