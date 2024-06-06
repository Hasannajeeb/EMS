from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from .models import Event
from django.utils.translation import gettext_lazy as _

from ems.users.models import User

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name='events/create_event_form.html'

event_create_view = EventCreateView.as_view()

class AllEventsListView(ListView):
    model = Event
    template_name = 'events/list_events.html'
    context_object_name = 'objects'

all_events_list_view = AllEventsListView.as_view()

class UserEventsListView(LoginRequiredMixin , ListView):
    model = Event
    template_name = 'events/list_events.html'
    context_object_name = 'objects'

    def get_query_set(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['enable_delete'] = True
        kwargs['enable_edit'] = True
        return kwargs

user_events_list_view = UserEventsListView.as_view()

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    slug_field = "id"
    slug_url_kwarg = "id"

event_detail_view = EventDetailView.as_view()

class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    fields = ["name","description","date","time","duration","venue"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.get_absolute_url()

event_update_view = EventUpdateView.as_view()

class EventDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    success_message = _("Event Deleted successfully")

event_delete_view = EventDeleteView.as_view()