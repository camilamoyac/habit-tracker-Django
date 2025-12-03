from django.shortcuts import render
from .models import Habit, DailyCheck
from datetime import date

def home(request):
    if not request.user.is_authenticated:
        return render(request, "habits/welcome.html")

    today = date.today()
    habits = Habit.objects.filter(user=request.user)

    checks = DailyCheck.objects.filter(habit__in=habits, date=today)
    done_ids = {c.habit_id for c in checks}

    return render(request, "habits/home.html", {
        "habits": habits,
        "done_ids": done_ids
    })
