from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from datetime import timedelta

from .models import Habit, HabitLog
from .forms import HabitForm

@login_required
def home(request):
    """
    Home page view for logged-in users.
    - Displays today's habits.
    - Creates a HabitLog for each habit if it doesn't exist for today.
    - Handles POST requests to toggle the 'done' status of a habit for today.
    """
    today = timezone.localdate() - timezone.timedelta(days=0)
    habits = Habit.objects.filter(user=request.user)

    # a HabitLog for each habit for today
    for habit in habits:
        HabitLog.objects.get_or_create(habit=habit, date=today)

    # all HabitLogs for today
    logs = HabitLog.objects.filter(habit__user=request.user, date=today).select_related('habit')

    if request.method == 'POST':
        log_id = request.POST.get('log_id')
        log = HabitLog.objects.get(id=log_id)
        log.done = not log.done  # toggle
        log.save()
        return redirect('home')

    return render(request, 'habits/home.html', {
    'logs': logs,
})

@login_required
def add_habit(request):
    """
    View to add a new habit for the logged-in user.
    - Handles GET requests by displaying an empty HabitForm.
    - Handles POST requests to save a new habit with the current user.
    """
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
    """
    Deletes a habit belonging to the logged-in user.
    - Redirects back to home after deletion.
    """
    habit = Habit.objects.get(id=habit_id, user=request.user)
    habit.delete()
    return redirect('home')

@login_required
def habit_logs(request):
    """
    Displays the Habit Logs page for the user.
    - Shows all habits and their logs.
    - Includes the current streak for each habit using Habit.get_streak().
    """
    habits = Habit.objects.filter(user=request.user)
    habit_entries = []

    for habit in habits:
        logs = HabitLog.objects.filter(habit=habit).order_by('-date')
        streak = habit.get_streak()
        habit_entries.append({
            'habit': habit,
            'logs': logs,
            'streak': streak,
        })

    return render(request, 'habits/habit_logs.html', {
        'habit_entries': habit_entries
    })

def register(request):
    """
    User registration view.
    - Displays a UserCreationForm on GET.
    - Creates a new user on POST if the form is valid.
    - Redirects to login after successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'habits/register.html', {'form': form})

def logout_view(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect('login')
