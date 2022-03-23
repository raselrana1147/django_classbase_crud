from dataclasses import fields
import django
from adminssion.models import Adminssion
from django.forms import ModelForm
from django import forms



class AdminssionForm(ModelForm):
    class Meta:
       model=Adminssion
       fields=['name','email','phone','father_name','mother_name','image']
    #    widgets={
    #                "name":forms.TextInput(attrs={'placeholder':'Name','name':'name','class':'form-control'}),
    #                'email':forms.EmailInput(attrs={'placeholder':'Enter your email','class':'form-control','name':'email'}),
    #                'phone':forms.TextInput(attrs={'placeholder':'Enter your phone number','class':'form-control','name':'phone'}),
    #                'father_name':forms.TextInput(attrs={'placeholder':'Enter your father name','class':'form-control','name':'father_name'}),
    #                'mother_name':forms.TextInput(attrs={'placeholder':'Enter your mother name','class':'form-control','name':'mother_name'}),
    #                'image':forms.FileInput(attrs={'class':'form-control','name':'image'}),
                   
                  
    #             }
      
      
       
       
       

    