from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]