import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from items.models import DEPARTMENT_CHOICES, FoundItem, LostItem


class Command(BaseCommand):
    help = "Seed 10 LostItem and 10 FoundItem test records."

    def handle(self, *args, **options):
        departments = [value for value, _ in DEPARTMENT_CHOICES]
        places = [
            "Main Gate",
            "Library",
            "Cafeteria",
            "Gymnasium",
            "Computer Lab",
            "Chapel",
            "Room 101",
            "Room 204",
            "Student Lounge",
            "Parking Area",
        ]
        item_names = [
            "Wallet",
            "ID Card",
            "Umbrella",
            "Backpack",
            "Calculator",
            "Phone",
            "Notebook",
            "Water Bottle",
            "Watch",
            "Jacket",
        ]
        people = [
            "Juan Dela Cruz",
            "Maria Santos",
            "Carlo Reyes",
            "Anne Lim",
            "Paolo Tan",
            "Bianca Cruz",
            "Marco Sy",
            "Lia Gomez",
            "Ryan Uy",
            "Nina Flores",
        ]

        today = timezone.now().date()

        for i in range(10):
            slug = people[i].lower().replace(' ', '.')
            LostItem.objects.create(
                name=f"{item_names[i]} (Lost {i + 1})",
                description=f"Sample lost item description #{i + 1}",
                lost_in=random.choice(places),
                lost_by=people[i],
                lost_by_email=f"{slug}{i + 1}@student.example.edu",
                department=random.choice(departments),
                date_lost=today - timedelta(days=random.randint(1, 30)),
            )

        for i in range(10):
            status = random.choice(["Unclaimed", "Claimed"])
            date_found = today - timedelta(days=random.randint(1, 30))
            claimed_by = None
            date_claimed = None

            claimed_by_email = None
            if status == "Claimed":
                claimed_by = random.choice(people)
                cslug = claimed_by.lower().replace(' ', '.')
                claimed_by_email = f"{cslug}@student.example.edu"
                date_claimed = date_found + timedelta(days=random.randint(1, 7))

            finder = random.choice(people)
            fslug = finder.lower().replace(' ', '.')
            FoundItem.objects.create(
                name=f"{item_names[i]} (Found {i + 1})",
                description=f"Sample found item description #{i + 1}",
                found_in=random.choice(places),
                found_by=finder,
                found_by_email=f"{fslug}{i}@student.example.edu",
                department=random.choice(departments),
                date_found=date_found,
                status=status,
                claimed_by=claimed_by,
                claimed_by_email=claimed_by_email,
                date_claimed=date_claimed,
            )

        self.stdout.write(self.style.SUCCESS("Created 10 lost items and 10 found items."))
