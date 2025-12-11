from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    target_streak = models.PositiveIntegerField(default=21)

    def __str__(self):
        return self.name
    
    def get_streak(self):
        """Return the current consecutive streak of done logs up to today."""
        logs = HabitLog.objects.filter(habit=self).order_by('-date')
        streak = 0
        for log in logs:
            if log.done:
                streak += 1
            else:
                break
        return streak

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    done = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'date')

