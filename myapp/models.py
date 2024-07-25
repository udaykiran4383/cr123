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
    name = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=10,default="")
    state = models.CharField(max_length=100,default="")
    district = models.CharField(max_length=100,default="")
    college = models.CharField(max_length=200,default="")
    year_of_study = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name
    
