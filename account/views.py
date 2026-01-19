from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from berserk.clients.account import Account
from general.client import ClientManager


class AccountView(View):
    def get(self, request, *args, **kwargs):
        client = ClientManager.get_client()
        data = client.account.get()  # Use client.account.get(), not Account(client)
        return HttpResponse(str(data))

