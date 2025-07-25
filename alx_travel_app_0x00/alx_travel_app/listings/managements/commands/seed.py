from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with listings"

    def handle(self, *args, **kwargs):
        titles = [
            "Luxury Villa in Banana Island",
            "Beachfront Bungalow",
            "Modern Loft in Lagos",
            "Mountain Retreat",
            "City Apartment with View"
        ]

        locations = ["Lagos", "Abuja", "Ibadan", "Port Harcourt", "Enugu"]

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description="This is a beautiful property for vacation or business stay.",
                location=random.choice(locations),
                price_per_night=random.randint(5000, 25000),
                max_guests=random.randint(1, 10)
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
