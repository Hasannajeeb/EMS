from django.forms import ModelForm
from .models import Event

class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['user']