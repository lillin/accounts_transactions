from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from website.models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('owner_name', 'owner_surname',)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('type', 'amount',)

    def validate(self, attrs):
        # forgot how to deal with foreign keys in serializers :(
        account_id = self.context.get('request').data.get('account')
        try:
            account_obj = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            raise ValidationError('There is no account with such ID')
        if attrs.get('type') == Transaction.TYPE_DEBIT and attrs.get('amount') > account_obj.balance:
            raise ValidationError('Insufficient funds to perform transaction')
        attrs['account'] = account_id
        return attrs


class AccountTransactionsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'type', 'amount', 'created_at',)


class AccountBalanceSerializer(serializers.ModelSerializer):
    transactions_amount = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('balance', 'transactions_amount',)

    def get_transactions_amount(self, obj):
        return obj.transaction_set.all().count()
