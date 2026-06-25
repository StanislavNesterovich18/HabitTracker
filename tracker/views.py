from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from tracker.models import HabitTracker
from tracker.serialisers import HabitTrackerCreateSerializer
from users.permissions import IsOwner


class HabitTrackerListApiViews(generics.ListAPIView):
    queryset = HabitTracker.objects.filter(is_public=True)
    serializer_class = HabitTrackerCreateSerializer

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitTrackerCreateSerializer

    def get_queryset(self):
        queryset = HabitTracker.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["create", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["retrieve", "update", "destroy", 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]
