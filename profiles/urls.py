from django.urls import path
from .views import Profiles, EditProfile


urlpatterns = [
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="edit_profile")
]
