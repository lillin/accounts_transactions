"""accounts_transactions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from website.views import TransactionViewSet, AccountBalanceView, AccountView, TransactionHistoryViewSet, IndexPageView

router = DefaultRouter()
router.register(r'transaction', TransactionViewSet)
router.register(r'account', AccountView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', IndexPageView.as_view()),
    url(r'^account-balance/$', AccountBalanceView.as_view()),
    url(r'^transactions-history/$', TransactionHistoryViewSet.as_view()),
    url('', include(router.urls))
]
