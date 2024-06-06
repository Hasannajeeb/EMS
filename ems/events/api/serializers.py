from rest_framework import serializers

from ems.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

        # extra_kwargs = {
        #     "url": {"view_name": "api:event-detail", "lookup_field": "pk"},
        # }
