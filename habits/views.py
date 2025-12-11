from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .models import Habit, HabitLog
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import HabitForm

@login_required
def home(request):
    today = timezone.localdate()
    habits = Habit.objects.filter(user=request.user)

    for habit in habits:
        HabitLog.objects.get_or_create(habit=habit, date=today)

    logs = HabitLog.objects.filter(habit__user=request.user, date=today)

    if request.method == 'POST':
        habit_id = request.POST.get('habit_id')
        log = HabitLog.objects.get(habit_id=habit_id, date=today)
        log.done = not log.done  # toggle
        log.save()
        return redirect('home')

    print("LOGS:", logs)
    print("HABITS:", habits)

    return render(request, 'habits/home.html', {
    'habits': habits,
    'logs': logs,
})

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('home')
    else:
        form = HabitForm()

    return render(request, 'habits/add_habit.html', {'form': form})

@login_required
def delete_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    habit.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'habits/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')