from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
#from django.contrib.auth.views import LogoutView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#class CustomLogoutView(LogoutView):
    #def get(self, request, *args, **kwargs):
        # Treat GET requests like POST to allow direct logout via URL
        #return self.post(request, *args, **kwargs)
# Create your views here




