from django.urls import path
from . import views
urlpatterns = [
    
    path('login-register',views.FormRender,name="login-register"),
    path('register',views.registerPage,name="register"),
    path('login',views.loginpage,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('registration',views.form_view,name='registration'),
    path('Doctor-register',views.Doctorregister,name='Doctor_register'),
    path('Patient-register',views.Patientregister,name='Patient_register'),

]