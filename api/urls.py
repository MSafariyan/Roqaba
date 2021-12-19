from django.urls import path
from . import views

urlpatterns = [
    path('get_book', views.get_book, name="get_book"),
    path('liveSearch', views.liveSearch, name="liveSearch"),
    path('chart', views.chart, name="show_chart")
]
