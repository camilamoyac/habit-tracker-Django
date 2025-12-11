from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Habit(models.Model):
    """
    Represents a habit created by a user.
    
    Attributes:
        user: ForeignKey to the Django User who owns this habit.
        name: The name/title of the habit.
        description: Optional detailed description of the habit.
        target_streak: Number of consecutive days the user aims to complete the habit.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    target_streak = models.PositiveIntegerField(default=21)

    def __str__(self):
        """
        Returns a string representation of the habit (its name).
        """
        return self.name
    
    def get_streak(self):
        """
        Calculates and returns the current consecutive streak of completed logs.
        
        Logic:
            - Orders HabitLog objects for this habit by date descending (latest first).
            - Iterates over the logs counting consecutive 'done' logs.
            - Stops counting when a log is not done.
            - Returns the streak count.
        """
        logs = HabitLog.objects.filter(habit=self).order_by('-date')
        streak = 0
        for log in logs:
            if log.done:
                streak += 1
            else:
                break
        return streak

class HabitLog(models.Model):
    """
    Represents a daily record of a habit's completion status.

    Attributes:
        habit: ForeignKey to the Habit this log belongs to.
        date: The date this log represents. Defaults to today.
        done: Boolean indicating whether the habit was completed on this date.

    Constraints:
        - unique_together ensures that each habit has only one log per date.
    """
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    done = models.BooleanField(default=False)

    class Meta:
        # Prevent duplicate logs for same habit/date
        unique_together = ('habit', 'date')

