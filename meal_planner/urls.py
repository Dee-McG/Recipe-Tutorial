from django.urls import path
from .views import MealPlanner


urlpatterns = [
    path("", MealPlanner.as_view(), name="meal_planner"),
]