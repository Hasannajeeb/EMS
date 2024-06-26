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
from django.urls import reverse

from ems.users.models import User
from .forms import EventCreateForm

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name='events/event_form.html'
    form_class=EventCreateForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
    template_name = 'events/event_details.html'
    context_object_name = 'obj'

event_detail_view = EventDetailView.as_view()

class EventDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    success_message = _("Event Deleted successfully")
    # success_url =reverse_lazy('events:user-events')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['return_url'] = reverse("events:user-events")
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse("events:user-events")

event_delete_view = EventDeleteView.as_view()

class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class=EventCreateForm
    success_message = _("Information successfully updated")
    template_name='events/event_form.html'

event_update_view = EventUpdateView.as_view()