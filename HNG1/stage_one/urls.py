
from django.urls import path
from .views import SlackTrackView
urlpatterns=[
    path('',SlackTrackView.as_view(),name='slack_track'),
]