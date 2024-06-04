rom django.urls import path

from .views import event_detail_view
from .views import event_update_view
from .views import event_list_view
from .views import list_user_events_view
app_name = "events"
urlpatterns = [
    path("~update/", view=event_update_view, name="update"),
    path("<int:pk>/", view=event_detail_view, name="detail"),
    path("events/", view=event_list_view, name="list"),
    path("user-events/", view=list_user_events_view, name="list-user-events"),
]