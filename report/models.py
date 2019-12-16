from django.db import models
from django.conf import settings
# Create your models here.


class Account(models.Model):
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT  # we cannot delete user with money
    )

    def deposit(self, total_price):
        self.balance += total_price
        self.save()

    def __str__(self):
        return f'{self.id} of {self.user.username}'


class Action(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='actions',
    )

    def __str__(self):
        return f'Account number {self.account.id} ' +\
            f'was changed on {str(self.amount)}'


# class Transaction(models.Model):
#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )
#     date = models.DateTimeField(auto_now_add=True)

#     account = models.ForeignKey(
#         Account,
#         on_delete=models.CASCADE
#     )

#     merchant = models.CharField(max_length=255)

#     def __str__(self):
#         return f'Account number {self.account.id} ' +\
#             f'sent {str(self.amount)} to {self.merchant}'

#     @classmethod
#     def make_transaction(cls, amount, account, merchant):
#         if account.balance < amount:
#             raise(ValueError('Not enough money'))

#         with transaction.atomic():
#             account.balance -= amount
#             account.save()
#             tran = cls.objects.create(
#                 amount=amount, account=account, merchant=merchant)

#         return account, tran


# class Transfer(models.Model):

#     from_account = models.ForeignKey(
#         Account,
#         on_delete=models.CASCADE,
#         related_name='from_account'
#     )

#     to_account = models.ForeignKey(
#         Account,
#         on_delete=models.CASCADE,
#         related_name='to_account'
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )
