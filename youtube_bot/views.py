from http.client import HTTPResponse
from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi
from django.views.decorators.http import require_http_methods


# youtube_bot/views.py
from .utils import seconds_to_hms, get_completion_from_messages

# ... rest of the views code ...

@require_http_methods(["POST"])
def get_subtitle_text(request):
    video_url = request.data.get('video_url')
    try:
        video_id = video_url.split("v=")[1]
        subtitles = YouTubeTranscriptApi.get_transcript(video_id)
        subtitle_text = ""
        for subtitle in subtitles:
            start_time = seconds_to_hms(subtitle['start'])
            end_time = seconds_to_hms(subtitle['duration'])
            subtitle_text += f"{start_time} - {end_time}: {subtitle['text']} ;"
    except Exception as e:
        return HTTPResponse({'error': f"Error: {e}"}, status=400)

    context = [
        {'role': 'system', 'content': f"""
        You are a youtube bot, a bot that answers questions from the subtitle file that you receive of the video.\
        You will get questions and you need to answer them according to the\
        the subtitles. If not present in it, then get then answer them accordingly but specify that.\
        You respond in a short, very conversational friendly style.\
        This is the subtitle of a youtube video: <{subtitle_text}>
        """}
    ]

    questions = request.data.get('questions', [])
    responses = []
    for question in questions:
        response = get_completion_from_messages(question, context)
        responses.append(response)

    return HTTPResponse({'responses': responses}, status=200)

# Create your views here.
def render_home_page(request):
    return render(request, 'index.html', {})