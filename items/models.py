from django.db import models


DEPARTMENT_CHOICES = [
    ('CON', 'CON'),
    ('YAL-CBA', 'YAL-CBA'),
    ('CAS', 'CAS'),
    ('COE', 'COE'),
    ('CCS', 'CCS'),
    ('CTH', 'CTH'),
    ('CED', 'CED'),
]


class LostItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    lost_in = models.CharField(max_length=200)
    lost_by = models.CharField(max_length=200, blank=True, null=True)
    lost_by_email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    date_lost = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='lostitems/', blank=True, null=True)

    def __str__(self):
        return self.name


class FoundItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    found_in = models.CharField(max_length=200, blank=True, null=True)
    found_by = models.CharField(max_length=200, blank=True, null=True)
    found_by_email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    date_found = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Unclaimed', 'Unclaimed'), ('Claimed', 'Claimed')],
        default='Unclaimed'
    )
    claimed_by = models.CharField(max_length=200, blank=True, null=True)
    claimed_by_email = models.EmailField(blank=True, null=True)
    date_claimed = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='founditems/', blank=True, null=True)

    def __str__(self):
        return self.name
