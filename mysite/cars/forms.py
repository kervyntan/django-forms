from django import forms

class ReviewForm (forms.Form):
    first_name = forms.CharField(label = "First Name", max_length = 100)
    last_name = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Email")
    review = forms.CharField(label = "Review")  
