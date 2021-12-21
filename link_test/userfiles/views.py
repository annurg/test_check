from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, UpdateForm
from .models import Client

# Create your views here.

def register(request):
    client = Client.objects.all()
    print(request.method)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            user = form.save()
            return redirect("/profile/")
            print('zzz')
            to_email = form.cleaned_data.get('email')
    else:
        form = SignupForm()
    return render(request, 'userfiles/signup1.html', {'form': form,
                                                 })

def profile(request):
    print((request.user))
    user = Client.objects.get(username=request.user)
    if not request.user.is_authenticated:
        return redirect('{}?next={}'.format ('/login/', '/login/'))
    else:
        # user = request.user
        initial = {'username': user.username,
                   'email': user.email,
                   'address': user.address,
                   }
        if request.method == 'POST':
            # user = request.user
            form = UpdateForm(request.POST, instance=user)
            print('gheihetueith', form.is_valid())
            if form.is_valid():
                user = form.save()
                print(user.email)
                initial = {'username': user.username,
                   'email': user.email,
                   'address': user.address,

                   }
                return render(request, 'userfiles/profile.html',{'form':UpdateForm(initial=initial),
                                                                    })
            return render(request, 'userfiles/profile.html',{'form':UpdateForm(initial=initial),
                                                            })
        return render(request, 'userfiles/profile.html',{'form':UpdateForm(initial=initial),
                                                            })
