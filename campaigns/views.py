from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Campaign
from .serializers import CampaignSerializer
from django.utils.dateparse import parse_date

@api_view(['GET'])
def campaign_search(request):
    """Search for campaigns based on start and end date.

    Args:
        request (Request): The request object containing query parameters.

    Returns:
        Response: A response containing the filtered campaigns.
    """
    start = request.GET.get('start')
    end = request.GET.get('end')
    campaigns = Campaign.objects.all()
    if start:
        start_date = parse_date(start)
        if start_date:
            campaigns = campaigns.filter(start_date__gte=start_date)
    if end:
        end_date = parse_date(end)
        if end_date:
            campaigns = campaigns.filter(end_date__lte=end_date)
    serializer = CampaignSerializer(campaigns, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)         
    