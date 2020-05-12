from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password_hash=models.CharField(max_length=20)

class Quiz(models.Model):
    name=models.CharField(max_length=30)

class Question(models.Model):
    name=models.CharField(max_length=30)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name='questions')

class Options(models.Model):
    name=models.CharField(max_length=100)
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    isCorrect=models.BooleanField()

