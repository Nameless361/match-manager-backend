from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "teams"


class Match(models.Model):

    class Status(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Scheduled"
        LIVE = "LIVE", "Live"
        COMPLETED = "COMPLETED", "Completed"

    home_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name="home_matches"
    )

    away_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name="away_matches"
    )

    home_score = models.PositiveSmallIntegerField(default=0)

    away_score = models.PositiveSmallIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
    class Meta:
        db_table = "matches"