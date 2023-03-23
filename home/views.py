from django.views.generic import ListView
from recipes.models import Recipe


class Index(ListView):
    template_name = 'home/index.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        return self.model.objects.all()[:3]
