from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    """
    Serializer for the Campaign model.
    Handles serialization, deserialization, and validation logic.
    """

    class Meta:
        model = Campaign
        fields = '__all__'
        read_only_fields = ['id', 'owner']

    def create(self, validated_data):
        """
        Assigns the authenticated user as the owner of the campaign.
        """
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        """
        Validates that the end_date is not before the start_date.
        """
        start = data.get('start_date')
        end = data.get('end_date')

        if start and end and end < start:
            raise serializers.ValidationError("End date cannot be before start date.")
        return data
