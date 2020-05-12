from django.shortcuts import render
from rest_framework.views import APIView
from quiz.models import *
from rest_framework.response import Response

# Create your views here.
class checkAnswer(APIView):
    def get(self, request):
        data = request.data
        try:
            correct_option = Options.objects.filter(isCorrect=True, Question=data.question_id)
            data={}
            payload={}
            if correct_option:
                data['name']=str(correct_option.name)
                payload['status']=200
                payload['message']='correct answer available'
                payload['data']=data
            else:
                payload['status'] = 400
                payload['message'] = 'correct answer unavailable'
                payload['data'] = data
        except:
            payload={}
            payload['status']=400
            payload['message']='question not available'
        return Response(payload)
                # temp[every.Bank_code] = [every.bank_name, every.netbanking, every.debit]

class getQuestions(APIView):
    def get(self, request):
        data=request.data
        try:
            questions_list=Question.objects.filter(quiz=data.quiz_id)
            questions=[]
            if questions_list:
                for every in questions_list:
                    questions.append((every.name))
            return Response(questions)
        except:
            payload={}
            payload['status']=400
            payload['message']='questions not available for this quiz'
            return Response(payload)
class getOptions(APIView):
    def get(self, request):
        data=request.data
        try:
            options_list=Options.objects.filter(question=data.questions_id)
            options=[]
            if options_list:
                for every in options_list:
                    options.append((every.name))
            return Response(options)
        except:
            payload={}
            payload['status']=400
            payload['message']='options not available for this questions'
            return Response(payload)


