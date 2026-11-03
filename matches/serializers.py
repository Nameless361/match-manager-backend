from rest_framework import serializers
from .models import Team, Match


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ["id", "name", "created_at"]


class MatchSerializer(serializers.ModelSerializer):

    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)

    home_team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source="home_team",
        write_only=True
    )

    away_team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source="away_team",
        write_only=True
    )

    class Meta:
        model = Match
        fields = [
            "id",
            "home_team",
            "away_team",
            "home_team_id",
            "away_team_id",
            "home_score",
            "away_score",
            "status",
            "created_at",
            "updated_at"
        ]

    def validate(self, data):
        home_team = data.get("home_team")
        away_team = data.get("away_team")

        if home_team and away_team and home_team == away_team:
            raise serializers.ValidationError(
                "A team cannot play against itself."
            )

        return data