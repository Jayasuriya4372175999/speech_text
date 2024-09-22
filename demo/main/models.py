from django.db import models

# Create your models here.
class Patient_details(models.Model):
    class SexChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(
        max_length=1,
        choices=SexChoices.choices,  # Defining the available choices
        default=SexChoices.MALE      # Default value if no choice is provided
    )
    dob = models.DateField()
    phone_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=200)