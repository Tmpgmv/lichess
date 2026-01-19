from django.shortcuts import render
from django.views.generic import TemplateView


class BoardView(TemplateView):
    template_name = "board/board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        BOARD_WIDTH = 10 # 8 + letters/numbers on both sides.
        context["rows"] = range(BOARD_WIDTH-1, -1, -1)
        context["columns"] = range(0, BOARD_WIDTH, 1)

        return context
