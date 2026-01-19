"""
URL configuration for lichess project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from account.views import AccountView
from board.views import BoardView
from django.conf import settings
from django.conf.urls.static import static

from game.views import CreateGameView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BoardView.as_view(), name="board"),
    path('create-game/', CreateGameView.as_view(), name="create-game"),
    path('account-get/', AccountView.as_view(), name="account"),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
