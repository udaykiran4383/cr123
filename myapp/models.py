from django.db import models

class College(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        unique_together = ('name', 'state', 'district')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    REPRESENTATIVE_CHOICES = [
        ('college', 'College'),
        ('school', 'School')
    ]

    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=10, default="")
    state = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=200, default="", blank=True, null=True)
    school = models.CharField(max_length=200, default="", blank=True, null=True)
    year_of_study = models.CharField(max_length=20, default="")
    representative_type = models.CharField(max_length=10, choices=REPRESENTATIVE_CHOICES, default='college')

    def __str__(self):
        return self.name
from django.db import models

class CollegeRepresentative(UserProfile):
    class Meta:
        proxy = True
        verbose_name = 'College Representative'
        verbose_name_plural = 'College Representatives'

class SchoolRepresentative(UserProfile):
    class Meta:
        proxy = True
        verbose_name = 'School Representative'
        verbose_name_plural = 'School Representatives'
