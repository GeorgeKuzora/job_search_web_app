"""
Contains companies app models.

Content: Company model, Address model.
"""
from django.db import models


class Company(models.Model):
    """
    Companies registered as jobs providers.

    Company model is used in jobs app.

    Attributes:
        title: models.CharField Company title.
        description: models.TextField Long description of the company.
        email: models.EmailField Company's email.
        phone: models.CharField Company's phone.
        address: models.ForeignKey('Address') Company's address.
    """
    title = models.CharField("company title", max_length=100)
    description = models.TextField("company description")
    email = models.EmailField("company email")
    phone = models.CharField("company phone", max_length=12)
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, verbose_name="address", null=True
    )

    class META:
        ordering = ["title"]
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.title


class Address(models.Model):
    """
    Registered addresses.

    Address model is used in jobs and users apps.

    Attributes:
        country: models.CharField(choices) Address country.
        region: models.CharField Address region.
        city: models.CharField Address city.
        srteet: models.CharField Address srteet.
        building: models.CharField Address building.
        room: models.CharField Address room.
    """

    class CountryChoices(models.TextChoices):
        RUSSIA = "RUS"
        KAZAKHSTAN = "KAZ"
        BELARUS = "BEL"

    country = models.CharField("country",
                               max_length=50,
                               choices=CountryChoices.choices)
    region = models.CharField("region", max_length=50)
    city = models.CharField("city", max_length=50)
    street = models.CharField("street", max_length=50)
    building = models.CharField("building", max_length=6)
    room = models.CharField("room", max_length=5)

    class META:
        ordering = ["city"]
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        return f"{self.country},{self.region}, {self.city}, {self.street}, {self.building}, {self.room}"
