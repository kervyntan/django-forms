from django import forms
from . import models
from django.forms import ModelForm

            #class ReviewForm (forms.Form):
             #   first_name = forms.CharField(label = "First Name", max_length = 100)
              #  last_name = forms.CharField(label = "Last Name")
               # email = forms.EmailField(label = "Email")
                #review = forms.CharField(label = "Review")  
class ReviewForm(ModelForm):
    class Meta: 
        model = models.Review # connect it to the model you want to POST to
        # fields = ['first_name' , 'last_name', 'star_rating'] # choose the fields you want the client to fill out
        fields = "_all_" # uses all fields from the model

        labels = {
            'first_name' : "FIRST NAME",
            'last_name' : "LAST NAME",
            'star_rating' : "STARS",
        }