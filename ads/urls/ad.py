from django.urls import path
from ads.views.ad import *

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),

]