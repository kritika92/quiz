from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^checkAnswer/', views.checkAnswer.as_view(), name='checkAnswer'),
    url(r'^getOptions/', views.getOptions.as_view(), name='getOptions'),
    url(r'^getQuestions/', views.getQuestions.as_view(), name='getQuestions'),

]