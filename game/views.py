from email.policy import default

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView

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


class ChallengeListView(TemplateView):
    template_name = "game/incoming_challenges.html"
    def get_context_data(self, **kwargs):
        client = ClientManager.get_client()
        incoming_challenges = client.challenges.get_mine().get('in')
        challenges = [{"challenger" : item.get("challenger").get("id"), "url" : reverse("accept", kwargs = {"id":item.get("id")})} for item in incoming_challenges]
        context = super().get_context_data(**kwargs)
        context["challenges"] = challenges
        return context



class AcceptChallengeView(TemplateView):
    template_name = "game/result.html"

    def get(self, request, *args, **kwargs):
        client = ClientManager.get_client()
        client.challenges.accept(kwargs.get("id"))
        return redirect(reverse("board"))

