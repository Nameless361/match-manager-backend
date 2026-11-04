from rest_framework import viewsets
from .models import Team, Match
from .serializers import TeamSerializer, MatchSerializer
from .permissions import ReadOnlyOrSuperuser


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by("name")
    serializer_class = TeamSerializer
    permission_classes = [ReadOnlyOrSuperuser]


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.select_related(
        "home_team",
        "away_team"
    ).all().order_by("-created_at")

    serializer_class = MatchSerializer
    permission_classes = [ReadOnlyOrSuperuser]