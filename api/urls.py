from django.urls import path
from .views import workout_list

urlpatterns = [
  path('workouts/', workout_list, name="workout-list")
]