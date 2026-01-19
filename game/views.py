from email.policy import default

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from game.form import GameForm
from general.client import ClientManager
from berserk.clients import Challenges



class CreateGameView(TemplateView):
    template_name = "game/create_game.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        rated = bool(request.POST.get("rated", False))
        variant = request.POST.get("variant")
        clock_limit = request.POST.get("clock_limit")
        clock_increment = request.POST.get("clock_increment")
        color = request.POST.get("color")

        client = ClientManager.get_client()
        result = client.challenges.create(
            username=username,
            rated=rated,
            variant=variant,
            clock_limit=clock_limit,
            clock_increment=clock_increment,
            color=color,
        )
        context = super().get_context_data(**kwargs)
        context["url"] = result.get("url")

        return render(request, 'game/result.html', context)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = GameForm()
        context["form"] = form
        return context



class SendMove(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")