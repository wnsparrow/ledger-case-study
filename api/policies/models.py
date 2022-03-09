import uuid

from django.db import models


class AutoPolicy(models.Model):
    class DriverGender(models.TextChoices):
        FEMALE = "female"
        MALE = "male"

    class DriverEmployment(models.TextChoices):
        EMPLOYED = "employed"
        HOMEMAKER = "homemaker"
        OTHER = "other_emp"
        RETIRED = "retired"
        STUDENT = "student"
        UNEMPLOYED = "unemployed"

    class DriverMaritalStatus(models.TextChoices):
        MARRIED = "married"
        SINGLE = "single"

    class DriverLocation(models.TextChoices):
        RURAL = "rural"
        SUBURBAN = "suburban"
        URBAN = "urban"

    class VehicleModel(models.TextChoices):
        COUPE = "coupe_cabriolet"
        HATCHBACK = "hatchback"
        OTHER = "other_model"
        PICKUP = "pickup"
        SEDAN = "sedan"
        SUV = "suv"
        VAN = "van"

    public_id = models.UUIDField(default=uuid.uuid4, unique=True)

    # Policy start year/month
    year = models.IntegerField()
    month = models.IntegerField()

    # Features
    driver_age = models.IntegerField()
    driver_gender = models.CharField(max_length=255, choices=DriverGender.choices)
    driver_employment = models.CharField(
        max_length=255, choices=DriverEmployment.choices
    )
    driver_marital = models.CharField(
        max_length=255, choices=DriverMaritalStatus.choices
    )
    driver_location = models.CharField(max_length=255, choices=DriverLocation.choices)
    vehicle_age = models.IntegerField()
    vehicle_model = models.CharField(max_length=255, choices=VehicleModel.choices)

    # Metrics
    insurance_premium = models.FloatField()
    insurance_claims = models.IntegerField()
    insurance_losses = models.FloatField()

    class Meta:
        verbose_name_plural = "Auto Policies"
