from django.contrib.auth.decorators import login_required
from ast import Return
from asyncio.windows_events import NULL
from cgitb import text
from email.mime import message
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utilis import get_intent,symptoms,predict_disease,precautionDictionary,description
from healthApp.randgenerator import rand
from .models import Usersymptoms,symptoms as Symptoms


# Create your views here.

@login_required
def chat_bot(request):
    return render(request,'chat-bot.html')

def home(request):
    content={"name":"devu","symptoms":symptoms}
    return render(request, 'healthica/homepage.html',content)
    #return HttpResponse('<h1>hello</h1>')

def get_response(request,intent,session):
    response=''
    print(intent)
    try:
        user_symptoms = Usersymptoms.objects.get(check_up_id=session["checkup_ID"])
    except Usersymptoms.DoesNotExist:
        user_symptoms = Usersymptoms(user=request.user,check_up_id=rand(6))
        user_symptoms.save()
    if intent == "greeting":
        response = 'Hey {}, what symptoms do you have? please enter one of your symptoms.(Ex. headache, vomiting etc.)'.format(request.user.first_name)
    elif intent == "ask_symptoms":
        try:
            main_symp=Symptoms.objects.get(symptom_name=session["message"])
            user_symptoms.my_symptoms.add(main_symp)
        except Symptoms.DoesNotExist:
            response='Please Enter correct Symptoms!'
            return response,session["checkup_ID"]
        response = "Enter one more symptom beside {}. (Enter 'No' if not)".format(session["message"])
    elif intent == "ask_symptoms-no":
        affected_symtoms=[]
        final_symptoms=[]
        for i in range(len(symptoms)):
            affected_symtoms.append(0)
        for i in range(user_symptoms.my_symptoms.count()):
            print(user_symptoms.my_symptoms.all()[1])
            affected_symtoms[symptoms.index(user_symptoms.my_symptoms.all()[i].symptom_name)]=1
            final_symptoms.append(
                user_symptoms.my_symptoms.all()[i].symptom_name)
        disease=predict_disease(affected_symtoms,final_symptoms)
        print(affected_symtoms,final_symptoms)
        response=["disease","You may have {} disease".format(disease),disease]

    elif intent == "end-chat":
        response = ''
    else:
        response='Invalid Message!'
    return response,user_symptoms.check_up_id


@csrf_exempt
def predict(request):
    text = json.loads(request.body)
    msg = text["message"]
    intent=get_intent(msg)
    res,checkupid=get_response(request,intent,text)
    if(res[0]=="disease"):
        message = {"reply": res[1], "checkup_ID": checkupid}
    else:
        message={"reply":res,"checkup_ID":checkupid}
    return HttpResponse(json.dumps(message), content_type='application/json')
