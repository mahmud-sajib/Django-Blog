from django.shortcuts import render,redirect

# SignUp forms module.
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'authentication/signup.html', context)
    
