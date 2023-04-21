from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    date_of_fee_submission = models.DateField()

    def __str__(self):
        return self.name
