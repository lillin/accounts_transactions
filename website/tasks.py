from accounts_transactions.celery import celery_website
from website.models import Account, Transaction


@celery_website.task()
def create_transaction(account_id, type_transaction, amount):
    account_obj = Account.objects.get(id=account_id)
    if type_transaction == Transaction.TYPE_CREDIT:
        account_obj.balance += amount
    else:
        account_obj.balance -= amount
    account_obj.save(update_fields=['balance', ])
    Transaction.objects.create(account=account_obj, type=type_transaction, amount=amount)
