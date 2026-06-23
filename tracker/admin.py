from django.contrib import admin

from .models import HabitTracker


@admin.register(HabitTracker)
class HabitTrackerAdmin(admin.ModelAdmin):
    """Настройки интерфейса администрирования для модели HabitTracker"""

    list_display = ("id",
                    "user",
                    "place",
                    "action",
                    "sign_pleasant_habit",
                    "time_complete",
                    "is_public"
                    )
