from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import followuser, user_info
from doubt.views import search
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        college = request.POST['college']
        year = request.POST['year']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User Exists')
                return redirect('/')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                extra_info = user_info.objects.create(
                    user=username, college=college, year=year)
                user.save()
                extra_info.save()
                messages.success(
                    request, 'User created.please login to continue')
                return redirect('/')
        else:
            messages.error(request, 'Password not Matching')
            return redirect('/')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'User Does not Exist')
            return redirect('/')

    else:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    profile = User.objects.filter(username__icontains=str(request.user))
    user_extra = user_info.objects.filter(user__contains=str(request.user))
    print(user_extra)
    params = {'profile': profile, 'extrainfo': user_extra}
    return render(request, 'accounts/profile.html', params)


def follow(req, profile_username):
    userid = User.objects.get(username=profile_username)
    foll = followuser.objects.create(profile=userid, followed_by=req.user)
    foll.save()


def unfollow(req, profile_username):
    userid = User.objects.get(username=profile_username)
    unfoll = followuser.objects.filter(profile=userid, followed_by=req.user)
    unfoll.delete()


def users_list(request):
    user = User.objects.exclude(username=str(request.user))
    profile_username = request.GET.get('id')
    decision = request.GET.get('decision')
    if decision == 'follow':
        follow(request, profile_username)
    elif decision == 'unfollow':
        unfollow(request, profile_username)
    for u in user:
        u.followed = False
        ob = followuser.objects.filter(profile=u, followed_by=request.user)
        if ob:
            u.followed = True

    return render(request, 'accounts/users.html', {'users': user})


def other_prof(request, id):

    if id != 'otherprof':
        profile_username=id
    else: 
        profile_username = request.POST.get('id')
    profile = User.objects.filter(
        username__icontains=str(profile_username))
    extra_info = user_info.objects.filter(
        user__contains=str(profile_username))
    decision = request.POST.get('decision')
    if decision == 'follow': 
        follow(request, profile_username)
    elif decision == 'unfollow':
        unfollow(request, profile_username)
    for u in profile:
        u.followed = False
        ob = followuser.objects.filter(profile=u, followed_by=request.user)
        if ob:
            u.followed = True

    params = {'profile': profile, 'extrainfo': extra_info}
    return render(request, 'accounts/others_profile.html', params)
