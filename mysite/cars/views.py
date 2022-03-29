from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.

def rental_review (request):
    # POST request --> FORM contents --> thank you

    if request.method == 'POST':
        form = ReviewForm(request.POST) # section 13, video 
        if form.is_valid():
            print(form.cleaned_data) # eg. cleaned_data =  {'first_name' : what the user passed in, 'last_name' : ... }
            return redirect(reverse('cars:thank_you'))


    else:
        form = ReviewForm() # if user visits the page for the first time (no submission yet/no POST request sent)

    return render(request, 'cars/rental_review.html', context={'form' : form})

def thank_you(request):
    return render(request, 'cars/thank_you.html')