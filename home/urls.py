from django.conf.urls.static import static
from django.urls import path

from djangoGameProject import settings
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # path("<int:id>", views.detail, name="detail")
   ]