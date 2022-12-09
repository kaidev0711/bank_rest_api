from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(
        Currency, related_name="transactions", on_delete=models.PROTECT
    )
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        related_name="transactions",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.amount} {self.currency.code} {self.date}"


class AllowList(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address
