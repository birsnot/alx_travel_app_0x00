from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random
from django.contrib.auth import get_user_model



class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create or get a host user
        User = get_user_model()

        host, created = User.objects.get_or_create(username="demo_host")

        if created:
            host.email = "demo@example.com"
            host.set_password("testpassword123")
            host.save()

        # Optional: Clear existing data
        Listing.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Creating sample listings..."))

        for _ in range(10):  # create 10 sample listings
            listing = Listing.objects.create(
                title=fake.company(),
                description=fake.text(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 300), 2),
                host=host,
                capacity=random.randint(1, 6),
            )
            self.stdout.write(self.style.SUCCESS(f"Created: {listing.title}"))

        self.stdout.write(self.style.SUCCESS("Seeding completed."))
