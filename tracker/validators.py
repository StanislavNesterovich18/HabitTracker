from datetime import timedelta

from rest_framework.exceptions import ValidationError


class ValidatorRelatedHabit:

    def __call__(self, attr):
        related_habit = attr.get("related_habit")
        reward = attr.get("reward")
        if related_habit and reward:
            raise ValidationError("Нельзя одновременно выбирать связанные привычки и указывать вознаграждения")


class ValidatorTimeComplete:

    def __call__(self, attr):
        time_complete = attr.get("time_complete")
        if time_complete >= timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не меньше 120 секунд.")


class ValidatorSignPleasantHabit:

    def __call__(self, attr):
        related_habit = attr.get("related_habit")
        if related_habit and not related_habit.sign_pleasant_habit:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")




class ValidatorReward:

    def __call__(self, attr):
        sign_pleasant_habit = attr.get("sign_pleasant_habit")
        reward = attr.get("reward")
        if sign_pleasant_habit and not reward:
           raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class ValidatorPeriodicity:

    def __call__(self, attr):
        periodicity = attr.get("periodicity")
        if periodicity and periodicity > timedelta(days=7):
           raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")



