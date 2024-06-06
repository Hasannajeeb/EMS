from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from ems.users.api.views import UserViewSet
from ems.events.api.views import EventViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("events", EventViewSet)


app_name = "api"
urlpatterns = router.urls
