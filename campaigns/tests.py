from django.test import TestCase
from drip.models import Drip
from campaigns.models import Campaign, CampaignDrip

DRIP_AMOUNT = 10


class DripsTestCase(TestCase):

    def test_campaings_creation(self):
        drips = [Drip(name='{}th drip'.format(i)) for i in range(DRIP_AMOUNT)]
        Drip.objects.bulk_create(drips)
        drips = Drip.objects.all()
        campaign = Campaign()
        campaign.save()
        campaign_drips = [CampaignDrip(campaign=campaign, drip=d) for d in drips]  # noqa: E501
        CampaignDrip.objects.bulk_create(campaign_drips)

        assert len(campaign.drips) == DRIP_AMOUNT