
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('recipelist/', views.view_recipe, name='view_recipe'),
    path('recipes/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('recipe/update/<int:recipe_id>/', views.update_recipe, name='update_recipe')
    
]