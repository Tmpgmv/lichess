from django.shortcuts import render
from django.views.generic import TemplateView

from general.client import ClientManager


class BoardView(TemplateView):
    template_name = "board/board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        BOARD_WIDTH = 10 # 8 + letters/numbers on both sides.
        context["rows"] = range(BOARD_WIDTH-1, -1, -1)
        context["columns"] = range(0, BOARD_WIDTH, 1)


        client = ClientManager.get_client()
        current_games = client.games.get_ongoing() # Games being played.


        for game in current_games:
            opponent = game.get("opponent")
            opponent_username = opponent.get("username")
            opponent_rating = opponent.get("rating")
            rated = game.get("rated")
            color = game.get("color")
            opponent_color = "black" if color is "white" else "white"

            context["opponent_username"] = opponent_username
            context["opponent_rating"] = opponent_rating
            context["rated"] = rated
            context["color"] = color
            context["opponent_color"] = opponent_color

            break # Only one game is allowed.



        return context
