from rest_framework.serializers import ModelSerializer

from tracker.models import HabitTracker
from tracker.validators import ValidatorRelatedHabit, ValidatorTimeComplete, ValidatorSignPleasantHabit, \
    ValidatorReward, ValidatorPeriodicity


class HabitTrackerCreateSerializer(ModelSerializer):
    class Meta:
        model = HabitTracker
        exclude = ("user",)
        validators = [
            ValidatorRelatedHabit(),
            ValidatorTimeComplete(),
            ValidatorSignPleasantHabit(),
            ValidatorReward(),
            ValidatorPeriodicity(),
        ]