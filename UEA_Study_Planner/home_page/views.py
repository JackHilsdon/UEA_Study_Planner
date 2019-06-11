from django.shortcuts import render
from django.http import HttpResponse



# Function that handles the traffic from the home-page of the app
def home(request):
	return render(request, 'home_page/home.html')

# Function that handles the traffic from the about-page of the app
def about(request):
	return render(request, 'home_page/about.html', {'title': 'About'})

