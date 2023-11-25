from django.shortcuts import get_object_or_404, redirect, render

from .models import Recipe
from .forms import RecipeForm

def create_recipe(request):
    context = {}
    form = RecipeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('view_recipe')
    context['form'] = form
    
    
    return render(request, 'create.html', context)

def view_recipe(request):
    recipes ={}

    recipes["recipes"] = Recipe.objects.filter(user=request.user)
    return(render(request,'recipelist.html',recipes))

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('view_recipe')
    
    return render(request, 'delete_recipe_confirm.html', {'recipe': recipe})

def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('view_recipe')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'update.html', {'form': form, 'recipe': recipe})