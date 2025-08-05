from rest_framework import serializers
from .models import Event
from apps.spaces.models import Space
from apps.spaces.serializers import SpaceSerializer

class EventSerializer(serializers.ModelSerializer):
    space_name = serializers.CharField(source='space.name', read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'id', 'event_name', 'start_datetime', 'end_datetime',
            'organizer_name', 'organizer_email', 'event_type', 
            'attendance', 'status', 'space', 'space_name'
        ]
        read_only_fields = ['id', 'status', 'space_name']

    def validate(self, data):
        """
        Validate the event data
        """
        start_datetime = data.get('start_datetime')
        end_datetime = data.get('end_datetime')

        # Validate datetime
        if start_datetime and end_datetime:
            if start_datetime >= end_datetime:
                raise serializers.ValidationError(
                    "End datetime must be after start datetime"
                )

        return data

class EventListSerializer(serializers.ModelSerializer):
    space_name = serializers.CharField(source='space.name', read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'id', 'event_name', 'start_datetime', 'end_datetime',
            'status', 'space_name'
        ]

from rest_framework import serializers
from .models import Booking
from apps.spaces.serializers import SpaceSerializer

class BookingSerializer(serializers.ModelSerializer):
    space_details = SpaceSerializer(source='space', read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 
            'event_name',
            'start_datetime', 
            'end_datetime',
            'organizer_name', 
            'organizer_email',
            'event_type',
            'attendance',
            'status',
            'user',
            'space',
            'space_details',
            'required_resources',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        """
        Check that start_datetime is before end_datetime.
        """
        if data['start_datetime'] >= data['end_datetime']:
            raise serializers.ValidationError("End datetime must be after start datetime")
        
        # Check for booking conflicts
        space = data['space']
        start = data['start_datetime']
        end = data['end_datetime']
        
        # Exclude current booking when updating
        booking_id = self.instance.id if self.instance else None
        
        conflicts = Booking.objects.filter(
            space=space,
            start_datetime__lt=end,
            end_datetime__gt=start
        )
        
        if booking_id:
            conflicts = conflicts.exclude(id=booking_id)
            
        if conflicts.exists():
            raise serializers.ValidationError("This space is already booked during the selected time period")
            
        return data