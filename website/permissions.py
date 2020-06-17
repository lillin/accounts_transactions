from rest_framework.permissions import BasePermission

from website.models import Account


class AccountExists(BasePermission):
    """
        Allow actions with transactions if account with corresponding ID exists
    """
    # TODO: simple jwt login required for feature
    def has_permission(self, request, view):
        pass
