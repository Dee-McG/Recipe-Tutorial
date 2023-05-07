from django.urls import path
from .views import MealPlanner, GetMeal, AddMeal


urlpatterns = [
    path("", MealPlanner.as_view(), name="meal_planner"),
    path("create_plan/<str:meal_date>/<str:meal_type>/", GetMeal.as_view(), name="get_meals"),
    path("create_meal/<str:meal_date>/<str:meal_type>/<int:pk>/", AddMeal.as_view(), name="add_meal"),
]