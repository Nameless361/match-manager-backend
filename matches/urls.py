from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, MatchViewSet

router = DefaultRouter()

router.register("teams", TeamViewSet)
router.register("matches", MatchViewSet)

urlpatterns = router.urls