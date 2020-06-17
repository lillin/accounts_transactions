import uuid

from django.db import models


class Account(models.Model):
    owner_name = models.CharField(max_length=50)
    owner_surname = models.CharField(max_length=50)
    balance = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    TYPE_CREDIT = 'credit'
    TYPE_DEBIT = 'debit'

    TYPE_SET = (
        (TYPE_CREDIT, 'credit-transaction'),
        (TYPE_DEBIT, 'debit-transaction'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, choices=TYPE_SET, default=TYPE_CREDIT)
    amount = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
