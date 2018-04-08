from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from apps.models import CreatePost
from apps.forms import Sign_up_form, Create_entry_form

@login_required(login_url = 'login/')
def home(request):
	posts_objs = CreatePost.objects.filter( autor = request.user).order_by("-id")
	lol = posts_objs.text()
	if lol >= 50:
		kek = lol[:50]
		
	return render(request, 'home_templates/home.html', {'posts_objs': posts_objs})

def sign_up(request):
	create_user = Sign_up_form()
	if request.method == 'POST':
		create_user = Sign_up_form(request.POST)
		if create_user.is_valid():
			user = User.objects.create_user(**create_user.cleaned_data)
			login(request, authenticate(
				username = create_user.cleaned_data['username'],
				password = create_user.cleaned_data['password']
				))
			return redirect(home)
	return render(request, 'sign_up_templates/sign_up_template.html', {'create_user':create_user})

@login_required(login_url = 'login/')
def CreateEntry(request):
	create_entry = Create_entry_form()
	if request.method == 'POST':
		create_entry = Create_entry_form(request.POST, request.FILES)
		if create_entry.is_valid():
			post = create_entry.save(commit = False)
			post.autor = request.user
			post.save()
			return redirect(home)
	return render(request, 'create_entry_templates/create_entry_template.html', {'create_entry': create_entry} )

@login_required(login_url = 'login/')
def EditEntry(request, entry_id):
	create_entry = Create_entry_form(instance = CreatePost.objects.get(id = entry_id))
	if request.method == 'POST':
		create_entry = Create_entry_form(request.POST, request.FILES, instance = CreatePost.objects.get(id = entry_id))
		if create_entry.is_valid():
			create_entry.save()
			return redirect(home)
	return render(request, 'entry_templates/entry_template.html', {'create_entry': create_entry})

@login_required(login_url = 'login/')
def read_entry(request, read_id):
	entry = CreatePost.objects.get(id = read_id)
	return render(request, 'read_entry_templates/read_entry_template.html', {'entry': entry})
# Create your views here.
