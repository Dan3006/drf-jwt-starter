from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def workout_list(request):
  sample_data = [
    {"exercise": "Squat", "weight": 180, "reps": 5},
    {"exercise": "Bench Press", "weight": 100, "reps": 8},
    {"exercise": "Deadlift", "weight": 220, "reps": 3},
  ]
  return Response(sample_data)