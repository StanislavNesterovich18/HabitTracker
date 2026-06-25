from django.urls import path
from rest_framework import routers

from tracker.apps import TrackerConfig
from tracker.views import HabitTrackerListApiViews, HabitViewSet

app_name = TrackerConfig.name
router = routers.DefaultRouter()
router.register(r'habits',HabitViewSet, basename='habit')
urlpatterns = [
    path("habits/public/", HabitTrackerListApiViews.as_view(), name="habits_public"),

] + router.urls