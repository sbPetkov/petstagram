from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.pets.forms import PetForm, PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet

#
# class AddPetView(CreateView):
# model = Pet
# form_class = PetCreateForm
# templates = 'pets/pet-add-page.html'
# success_url = reverse_lazy('details pet', username='Svilen, pet_slug')


def add_pet(request):
    form = PetCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            created_pet = form.save()
            return redirect('details pet', username='Svilen', pet_slug=created_pet.slug)

    context = {
        'pet': form
    }
    return render(request, 'pets/pet-add-page.html', context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    context = {
        "pet": pet
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'username': username,
        'pet': pet
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet_form.save()
        return redirect('index')

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet
    }
    return render(request, 'pets/pet-delete-page.html', context)
