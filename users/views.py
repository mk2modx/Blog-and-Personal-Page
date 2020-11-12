from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    print('in register')
    if request.method == 'POST':
        print('in post')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('in valid')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            print(username)
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
