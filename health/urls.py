from unicodedata import name
from django.urls import path
from . import views

#from .utilis import update_symptoms

urlpatterns = [
    path('chat-bot', views.chat_bot, name='chat_bot'),
    path('predict', views.predict, name='predict'),
    path('home',views.home,name='home'),
    path('diabetes-predict', views.diabetes_view, name='diabetes-predict'),
    path('diabetes-result', views.diabetes, name='predicteddiabetes'),
    path('pedigree',views.pedigree,name="pedigree"),
    path('heart-disease',views.heartdisease, name='ecg')
    #path('save-symp',update_symptoms,name='symptoms-update'),
]

