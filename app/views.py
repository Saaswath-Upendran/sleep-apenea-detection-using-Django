from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.forms import UserCreationForm
from sklearn.preprocessing import StandardScaler
import numpy as np
from django.http import *
from .forms import *
from django.urls import reverse_lazy
from .models import * 
import pickle
# Create your views here.
model = pickle.load(open('model.pkl',"rb"))


class HomeView(TemplateView):
    template_name = "index.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "siginup.html"



def PredictionView(request):

    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            scale = StandardScaler()
            data = [form.data["age"],form.data["sex"],form.data["cp"],form.data["tresbps"],form.data["chol"],form.data["fbs"],form.data["restecg"],form.data["thalach"],form.data["exang"],form.data["oldpeak"],form.data["slope"],form.data["ca"],form.data["thal"]]
            predict = scale.fit_transform(np.array(data,ndmin=2))
            final = model.predict(predict)
            return render(request,"final.html",{"final":final})
        else:
            HttpResponse(form.errors)
    else:
        form = PredictionForm()
        return render(request,"prediction.html",{"form":form})

def aboutus(request):
    return render(request,"aboutus.html")