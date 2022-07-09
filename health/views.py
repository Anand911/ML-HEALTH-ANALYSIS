from cmath import e
from errno import EEXIST
from unicodedata import name
from django.contrib.auth.decorators import login_required
from ast import Return
from asyncio.windows_events import NULL
from cgitb import text
from email.mime import message
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utilis import get_intent,symptoms,predict_disease,precautionDictionary,description, predict_diabetes
from healthApp.randgenerator import rand
from .models import Usersymptoms,symptoms as Symptoms
import pickle
from .Ecg import  ECG
#intialize ecg object

#from .models import predict_diabetes

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




def diabetes_view(request):
    return render(request, 'diabeticform.html')

def diabetes(request):
    if request.method=="POST":
        Glucoselevel=request.POST.get('Glucose Level')
        Insulin=request.POST.get('Insulin')
        bmi=request.POST.get('BMI')
        DiabetesPF=request.POST.get('Diabetes PF')
        Age=request.POST.get('Age')
        r=predict_diabetes(request)#)
        return r
        #en.save()
        #return render(request,'result.html'



def heartdisease(request):

    #get the uploaded image
    if request.method=='POST':
        #intialize ecg object
        ecg = ECG()
        #get the uploaded image
        uploaded_file = request.FILES['ecg']
        if uploaded_file is not None:
            """#### **UPLOADED IMAGE**"""
            # call the getimage method
            ecg_user_image_read = ecg.getImage(uploaded_file)
            #show the image
            

            """#### **GRAY SCALE IMAGE**"""
            #call the convert Grayscale image method
            ecg_user_gray_image_read = ecg.GrayImgae(ecg_user_image_read)
            
            
            
            """#### **DIVIDING LEADS**"""
            #call the Divide leads method
            dividing_leads=ecg.DividingLeads(ecg_user_image_read)

            
            
            """#### **PREPROCESSED LEADS**"""
            #call the preprocessed leads method
            ecg_preprocessed_leads = ecg.PreprocessingLeads(dividing_leads)

        
            
            """#### **EXTRACTING SIGNALS(1-12)**"""
            #call the sognal extraction method
            ec_signal_extraction = ecg.SignalExtraction_Scaling(dividing_leads)
            
            """#### **CONVERTING TO 1D SIGNAL**"""
            #call the combine and conver to 1D signal method
            ecg_1dsignal = ecg.CombineConvert1Dsignal()
            
                
            """#### **PERFORM DIMENSINALITY REDUCTION**"""
            #call the dimensinality reduction funciton
            ecg_final = ecg.DimensionalReduciton(ecg_1dsignal)
            
            
            """#### **PASS TO PRETRAINED ML MODEL FOR PREDICTION**"""
            #call the Pretrainsed ML model for prediction
            ecg_model=ecg.ModelLoad_predict(ecg_final)
            return render(request,'heartdisease.html',{'prediction':ecg_model})
    else:
        return render(request,'heartdisease.html')













