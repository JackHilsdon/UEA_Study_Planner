from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def registerNewAcc(request):
	#If receiving a POST request
	if request.method == 'POST':
		# Create a new instance of our form that contains POST request data
		signUpForm = UserRegistrationForm(request.POST)
		# Validation check that the data inputted was successful
		if signUpForm.is_valid():
			signUpForm.save()
			username = signUpForm.cleaned_data.get('username')
			messages.success(request, f'Account successfully created for: {username}! Please login:')
			return redirect('login')
	#Creating an instance of the inbuilt python class UserCreationFor
	else:
		signUpForm = UserRegistrationForm()
	return render(request, 'users/registration.html', {'form' : signUpForm})

#Decorator to check if a user is logged in before they can access the profile page
@login_required
def userProfile(request):
	return render(request, 'users/profile.html')


