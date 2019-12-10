# pylint: disable=too-few-public-methods
"""Models for bills application."""

from djmoney.models.fields import MoneyField
from django.db import models


class Participant(models.Model):
    """Model for event's participants."""

    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Event(models.Model):
    """Settlement for whole event, eg. kayaks."""

    name = models.CharField(max_length=500, unique=True)
    paymaster = models.ForeignKey(
        Participant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="paymaster",
    )
    participants = models.ManyToManyField(Participant, related_name="participates")

    def __str__(self):
        return self.name


class Bill(models.Model):
    """Single bill, eg. for car, food, fuel etc."""

    title = models.CharField(max_length=100)
    amount = MoneyField(
        max_digits=7, decimal_places=2, default_currency="PLN", default=0
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    payer = models.ForeignKey(
        Participant,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="payer",
    )
    participants = models.ManyToManyField(Participant, related_name="bills")

    def __str__(self):
        return self.title


class Payment(models.Model):
    """Payment from one to another."""

    title = models.CharField(max_length=500)
    issuer = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="paid"
    )
    acquirer = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="acquired"
    )
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    amount = MoneyField(
        max_digits=7, decimal_places=2, default_currency="PLN", default=0
    )

    def __str__(self):
        return "{} to {} for {} ({})".format(
            self.issuer, self.acquirer, self.title, self.event
        )
