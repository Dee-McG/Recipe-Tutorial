from django.urls import path
from .views import AddRecipe


urlpatterns = [
    path('', AddRecipe.as_view(), name='add_recipe'),
]