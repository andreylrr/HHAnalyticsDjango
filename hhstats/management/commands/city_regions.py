from django.core.management.base import BaseCommand
from hhstats.models import Regions,Vacancies
import requests as req
import json
import os

class Command(BaseCommand):
    help = 'Make corrections on Regions table'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        db_regions = Regions.objects.order_by("vac_city").all()
        previous_region = db_regions[0]
        for region in db_regions[1:]:
            if region.vac_city == previous_region.vac_city:
                Vacancies.objects.filter(region=region.id).update(region=previous_region.id)
                print(f"Region id {previous_region.id} was corrected.")
            else:
                previous_region = region
