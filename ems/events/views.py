from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

from ems.users.models import User

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    slug_field = "id"
    slug_url_kwarg = "id"


event_detail_view = EventDetailView.as_view()


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    fields = ["name","description","date","time","duration","venue"]
    success_message = _("Information successfully updated")

    # def get_success_url(self):
    #     return self.object.get_absolute_url()

    # def get_object(self):
    #     return self.object


event_update_view = EventUpdateView.as_view()


class EventListView(ListView):
    model = Event

event_list_view = EventListView.as_view()

class ListUserEventsView(LoginRequiredMixin ,ListView):
    model = Event

    def get_query_set(self):
        return self.model.object.filter(user=self.request.user).all()

list_user_events_view = ListUserEventsView.as_view()

