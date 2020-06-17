from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import OrderingFilter

from website.models import Transaction, Account
from website.serializers import TransactionSerializer,  AccountTransactionsHistorySerializer, \
    AccountBalanceSerializer, AccountSerializer
from website.tasks import create_transaction


class TransactionViewSet(ModelViewSet):
    """
        Find transaction by ID;
        Commit new transaction to the account
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['get', 'post']

    # def get_queryset(self, *args, **kwargs):
    #     return Transaction.objects.filter(id=self.kwargs.get('transaction_id'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'type': request.data.get('type'),
                                               'amount': request.data.get('amount')})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # TODO: fix .delay for this celery task
        create_transaction(serializer.validated_data['account'],
                           serializer.validated_data['type'],
                           serializer.validated_data['amount'])


class TransactionHistoryViewSet(ListAPIView):
    """
        Fetches transactions history
    """
    queryset = Transaction.objects.all()
    serializer_class = AccountTransactionsHistorySerializer
    filter_backends = (OrderingFilter,)
    filter_fields = ('created_at',)


class AccountView(CreateAPIView, GenericViewSet):
    """
        Creates account
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountBalanceView(ListAPIView):
    """
        Fetches current account balance
    """
    queryset = Account.objects.all()
    serializer_class = AccountBalanceSerializer


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all()
        return self.render_to_response(context)
