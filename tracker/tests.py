import os
from datetime import timedelta
from unittest import TestCase

import django
from django.urls import reverse
from rest_framework import status

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from tracker.models import HabitTracker
from users.models import User
from rest_framework.test import APITestCase


class TrackerTestCase(APITestCase):

    id_lesson = 0

    def setUp(self):
        """Выполняется перед каждым тестом: готовим данные."""
        super().setUp()
        self.user = User.objects.create(
            email="test@test.com",
        )
        self.habit = HabitTracker.objects.create(
            user=self.user,
            place="Двор",
            time_success=timedelta(seconds=120),
            action="Присесть 100",
            periodicity=str(timedelta(seconds=120)),
            reward="Пирог",
            time_complete=str(timedelta(seconds=120))
        )
        self.client.force_authenticate(user=self.user)

    def test_tracker(self):
        url = reverse("tracker:habit-list")
        response = self.client.post(
            url, data={
                "user": self.user.pk, "place": "Двор", "sign_pleasant_habit":True,
                "time_success":timedelta(seconds=120), "action":"Присесть 100",
                "periodicity":timedelta(seconds=120),
                "time_complete":timedelta(seconds=110)
            }
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["place"], "Двор")

    def test_user_create(self):
        url = reverse("users:Create_user")
        response = self.client.post(
            url, data={
                "email": "test@test.ru",
                "password": "1234",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserManagerTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError) as e:
            User.objects.create_user(email=None, password='testpass')
        self.assertEqual(str(e.exception), "Email должен быть указан")

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_create_superuser_without_staff(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='admin@example.com',
                password='adminpass123',
                is_staff=False
            )




