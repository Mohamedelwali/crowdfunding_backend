from django.test import TestCase
from django.urls import reverse
from .models import Campaign
from users.models import User
from datetime import date

class CampaignSearchViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Test", last_name="User", email="test@example.com", password="pass", phone_number="01012345678"
        )
        Campaign.objects.create(
            title="Campaign 1",
            description="Desc 1",
            target_amount=1000,
            start_date=date(2025, 6, 1),
            end_date=date(2025, 7, 1),
            owner=self.user
        )
        Campaign.objects.create(
            title="Campaign 2",
            description="Desc 2",
            target_amount=2000,
            start_date=date(2025, 8, 1),
            end_date=date(2025, 9, 1),
            owner=self.user
        )

    def test_search_campaigns_by_date(self):
        url = reverse('project-search')
        response = self.client.get(url, {'start': '2025-06-01', 'end': '2025-07-01'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['title'], "Campaign 1")