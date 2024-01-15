from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
#  ]

def loginPage(request):
    page = 'login'

    # Prevent user from reaching login page if already logged in
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create a user instance but don't save it yet
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # Automatically login user after registration
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    # Searching rooms using q lookup
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    # If the current user is not the host of the room, deny access
    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            # Save the form data to update the existing room
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    # If the current user is not the host of the room, deny access
    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        # Delete the room if the request method is POST
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
