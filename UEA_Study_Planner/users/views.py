from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import ToDo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import csv, io


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
def toDoList (request):
	context = {
		'posts': ToDo.objects.all()
	}
	return render(request, 'users/todo.html', context)

class ToDoListView(LoginRequiredMixin, ListView):
	model = ToDo
	template_name = 'users/todo.html'
	context_object_name = 'posts'
	ordering = ['-date_created']



class ToDoDetailView(LoginRequiredMixin, DetailView):
	model = ToDo


class ToDoCreateView(LoginRequiredMixin, CreateView):
	model = ToDo
	fields = ['module_title', 'topic', 'notes']

	def form_valid(self, form):
		#setting the form author to the current logged in user
		form.instance.author=self.request.user
		return super().form_valid(form)


class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ToDo
	fields = ['module_title', 'topic', 'notes']


	def form_valid(self, form):
		#setting the form author to the current logged in user
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		todo = self.get_object()
		if self.request.user == todo.author:
			return True
		return False

class ToDoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = ToDo
	success_url = '/todo'
	
	def test_func(self):
		todo = self.get_object()
		if self.request.user == todo.author:
			return True
		return False

def semester_upload(request):
	template = "users/semester_upload.html"
	prompt = {
		'order': 'Order of the .csv file should be module_title, topic, notes, user_id.'
		}
	
	if request.method == "GET":
		return render(request, template, prompt)
	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		prompt2 = {
		'incorrect': 'That was an incorrect file type, please ensure you only upload .csv files!'
		}
		return render(request, template, prompt2)
		messages.error(request, 'Not a valid .csv file, please upload a correct .csv file!')
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
 		_, created = ToDo.objects.update_or_create(
 			module_title=column[0],
			topic=column[1],
			notes=column[2],
			author_id=column[3]
		)
	prompt3 = {
	'success': 'Your semester file has been successfully uploaded! You can now view your events in To Do List:'
	}
	return render(request, template, prompt3)
