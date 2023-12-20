from django.urls import path
from app_crud_clients import views
urlpatterns = [
    # <dominio.com>/...
    path(route="", view=views.home, name="home"),
]
