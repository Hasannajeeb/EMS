from django.urls import path

from .views import event_detail_view
from .views import event_update_view
from .views import all_events_list_view
from .views import user_events_list_view
from .views import event_create_view
from .views import event_delete_view

app_name = "events"
urlpatterns = [
    path("all-events/", view=all_events_list_view, name="all-events"),
    path("user-events/", view=user_events_list_view, name="user-events"),
    path("create-event/", view=event_create_view, name="create-event"),
    path("<int:pk>/", view=event_detail_view, name="detail"),
    path('<int:pk>/delete-event/', view=event_delete_view, name="delete"),
    # path("~update/", view=event_update_view, name="update"),
]