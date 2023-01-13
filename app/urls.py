from django.urls import path
from .views import *


app_name = "app"

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("SignUp/",SignUpView.as_view(),name="siginup"),
    path("Prediction/",PredictionView,name='prediction'),
    path("aboutus",aboutus,name="aboutus")
]