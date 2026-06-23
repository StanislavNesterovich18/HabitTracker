from django.db import models


class HabitTracker(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    place = models.CharField(max_length=200, blank=True, null=True, verbose_name="Место")
    time_success = models.DurationField(verbose_name="Время когда необходимо выполнить привычку")
    action = models.TextField(blank=True, null=True, verbose_name="Действие")
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки ")
    related_habit = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Связанная привычка", null=True, blank=True)
    periodicity = models.DurationField(verbose_name="Периодичность")
    reward = models.TextField(blank=True, null=True, verbose_name="Вознаграждение")
    time_complete = models.DurationField(blank=True, null=True, verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Трекер привычек"
        verbose_name_plural = "Трекеры привычек"


