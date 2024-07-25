from django.db import models

class UserProfile(models.Model):
    cr_id = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    whatsapp = models.CharField(max_length=200, default="")
    year = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    in_team = models.BooleanField(default=False)
    ref = models.CharField(max_length=200, default="")
    bonus_ref = models.CharField(max_length=200, default="")
    is_individual = models.BooleanField(default=False)
    tname = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
